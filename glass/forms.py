from django import forms
from django.forms import ModelForm
from models import *


class SlideForm(ModelForm):
    class Meta:
        model = Slide
        #exclude = ("foto",)
       
class MensajebForm(ModelForm):
    class Meta:
        model = Mensajeb
        exclude = ("foto",)
        
class InfoForm(ModelForm):
    class Meta:
        model = Info

class ContactosForm(ModelForm):
    class Meta:
        model = Contactos
        
class ServiciosForm(ModelForm):
    class Meta:
        model = Servicios
        
class FotosForm(ModelForm):
    class Meta:
        model = Fotos

class ServiPrinForm(ModelForm):
    class Meta:
        model =ServiPrin
        
class VisitasForm(ModelForm):
    class Meta:
        model =ServiPrin