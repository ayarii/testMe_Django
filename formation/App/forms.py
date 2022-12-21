from django import forms
from django.forms import Textarea

from.models import Projet
class AjoutForm(forms.ModelForm):
    
    class Meta:
        model = Projet
       # fields = ("nom_projet","duree_projet","createur","temps_alouee","superviseur")
       # widgets={'nom_projet':Textarea(
       #     attrs={'cols':20,'rows':10}
      #  )}
        fields=('__all__')
        exclude=('membres',)