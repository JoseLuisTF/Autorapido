from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.anuncio.models import Anuncio, Vehiculo
from apps.anuncio.forms import VehiculoForm, AnuncioForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return HttpResponse("Anuncios")


class AnuncioList(ListView):
    model = Anuncio
    template_name = 'anuncio/anuncio_list.html'


class AnuncioDetail(DetailView):
    model = Anuncio
    template_name = 'anuncio/anuncio_detalles.html'


class AnuncioCreate(CreateView):
    model = Anuncio
    template_name = 'anuncio/anuncio_form.html'
    form_class = AnuncioForm
    second_form_class = VehiculoForm
    success_url = reverse_lazy('anuncio:anuncio_listar')

    def get_context_data(self, **kwargs):
        context = super(AnuncioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES or None)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            anuncio = form.save(commit=False)
            anuncio.vehiculo = form2.save()
            anuncio.vendedor = request.user
            anuncio.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class AnuncioUpdate(UpdateView):
    model = Anuncio
    second_model = Vehiculo
    template_name = 'anuncio/anuncio_form.html'
    form_class = AnuncioForm
    second_form_class = VehiculoForm
    success_url = reverse_lazy('anuncio:anuncio_listar')

    def get_context_data(self, **kwargs):
        context = super(AnuncioUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        anuncio = self.model.objects.get(id=pk)
        vehiculo = self.second_model.objects.get(placa=anuncio.vehiculo.placa)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2'not in context:
            context['form2'] = self.second_form_class(instance=vehiculo)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_anuncio = kwargs['pk']
        anuncio = self.model.objects.get(id=id_anuncio)
        vehiculo = self.second_model.objects.get(placa=anuncio.vehiculo.placa)
        form = self.form_class(request.POST, request.FILES or None, instance=anuncio)
        form2 = self.second_form_class(request.POST, instance=vehiculo)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class AnuncioDelete(DeleteView):
    model = Anuncio
    template_name = 'anuncio/anuncio_delete.html'
    success_url = reverse_lazy('anuncio:anuncio_listar')


def anuncios_search(request):

    anuncio = Anuncio.objects.all()
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        anuncio = anuncio.filter(
                                    Q(vehiculo__marca__icontains=search_term) |
                                    Q(vehiculo__modelo__icontains=search_term))

    contexto = {'anuncios': anuncio}

    return render(request, 'anuncio/anuncio_list.html', contexto)

@login_required
def anuncios_usuario(request):

    anuncio = Anuncio.objects.all()
    anuncio = anuncio.filter(vendedor_id=request.user)

    contexto = {'anuncios': anuncio}

    return render(request, 'anuncio/anuncio_list.html', contexto)
