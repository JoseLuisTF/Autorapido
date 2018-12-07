from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from apps.usuario.forms import ProfileForm


from django.db import transaction


@transaction.atomic
def create_user_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
