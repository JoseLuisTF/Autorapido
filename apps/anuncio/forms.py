from django import forms

from apps.anuncio.models import Vehiculo, Anuncio


class VehiculoForm(forms.ModelForm):

    class Meta:

        model = Vehiculo

        fields = [
            'placa',
            'marca',
            'modelo',
            'anio',
            'color',
            'kilometraje',
            'cilindraje',
            'nPuertas',
            'aireAcondicionado',
            'vidriosElectricos',
            'tipoDireccion',
            'tipoTransmision',
            'airbag',
            'nAsientos',
            'alarma',
            'sunroof',
        ]
        labels = {
            'placa': 'Placa',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'anio': 'Año',
            'color': 'Color',
            'kilometraje': 'Kilometraje',
            'cilindraje': 'Cilindraje',
            'nPuertas': 'Numero de puertas',
            'aireAcondicionado': 'Aire Acondicionado',
            'vidriosElectricos': 'Vidrios Electricos',
            'tipoDireccion': 'Tipo Direccion',
            'tipoTransmision': 'Tipo Transmision',
            'airbag': 'Airbag',
            'nAsientos': 'Numero de asientos',
            'alarma': 'Alarma',
            'sunroof': 'Sunroof',
        }
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'cilindraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'nPuertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'aireAcondicionado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'vidriosElectricos': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'tipoDireccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoTransmision': forms.TextInput(attrs={'class': 'form-control'}),
            'airbag': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'nAsientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'alarma': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'sunroof': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class AnuncioForm(forms.ModelForm):
    class Meta:

        model = Anuncio

        fields = [
            'titulo',
            'precio',
            'negociable',
            'descripcion',
            'ubicacionDepartamento',
            'ubicacionCiudad',
            'imagen'
        ]

        labels = {
            'titulo': 'Titulo',
            'precio': 'Precio',
            'negociable': 'Precio Negociable',
            'descripcion': 'Descripcion',
            'ubicacionDepartamento': 'Departamento',
            'ubicacionCiudad': 'Ciudad',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'negociable': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'ubicacionDepartamento': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacionCiudad': forms.TextInput(attrs={'class': 'form-control'}),
        }

