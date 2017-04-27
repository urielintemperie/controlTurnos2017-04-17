from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.db.models import Q
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
    def clean_nombre(self):
        print ("clean nombre")
        cd = self.cleaned_data
        nombre = cd.get('nombre')
        if len(nombre) < 3 :
            raise forms.ValidationError("Nombre muy corto")
        return nombre

class medicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'estaActivo': forms.HiddenInput()
        }


class tratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class especialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ('nombre',)
#('estado', 'medico', 'paciente', 'horario', 'tratamiento',)

class obraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = ('nombre',)


class turnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'estaActivo': forms.HiddenInput(),
            'horarios': forms.HiddenInput()
            }

class turnoNuevoMagiaForm(forms.ModelForm):
    #horaInicio = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'time start ui-timepicker-input', 'value' : '8:00am'}))
    #horaFin = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'time end ui-timepicker-input', 'value' : '8:15am'}))
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            #'estaActivo': forms.HiddenInput(),
            #'dia' : forms.DateInput(attrs={'autocomplete' : 'off'}),
            'dia' : DateInput(),
            'horaInicio': forms.TextInput(attrs={'class' : 'time start ui-timepicker-input', 'value' : '8:00am'}),
            'horaFin' : forms.TextInput(attrs={'class' : 'time end ui-timepicker-input', 'value' : '8:15am'})
            #'horarios': forms.HiddenInput(),
            }
    '''my_field = forms.DateField(widget = AdminDateWidget)
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])'''
    '''
    class Meta:
        model = Turno
        fields = '__all__'
'''
    def clean(self):
        medico = self.cleaned_data.get('medico')
        dia = self.cleaned_data.get('dia')
        horaInicio = self.cleaned_data.get('horaInicio')
        horaFin = self.cleaned_data.get('horaFin')
        if Turno.objects.filter(medico=medico,dia=dia,horaInicio=horaInicio,horaFin=horaFin).exists():
            raise forms.ValidationError("Turno ya tomado")


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
    horaInicio = forms.TimeField()
    horaFin = forms.TimeField()

class CreacionTurnoNormalForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
    horaInicio = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'time start ui-timepicker-input', 'value' : '8:00am'}))
    horaFin = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'time end ui-timepicker-input', 'value' : '8:15am'}))
    '''class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'estaActivo': forms.HiddenInput()
            }'''

class LoginForm(forms.Form):
    username = forms.CharField(label="usuario", max_length=64)
    password = forms.CharField(label="clave", widget=forms.PasswordInput, max_length=64)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
            if not check_password(password, user.password):
                raise forms.ValidationError('Password incorrecto')
        except User.DoesNotExist:
            raise forms.ValidationError("No existe el usuario")
        return user


    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        if not valid:
            return valid
        return True
