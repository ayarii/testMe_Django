from django.shortcuts import render,HttpResponse
from App.models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import AjoutForm
# Create your views here.
def index(request):
    return HttpResponse("Bonjour Asma")
def home(request,up):
#return HttpResponse("Bonjour "+up)
    return HttpResponse(f"Bonjour UP{up}")
# 1ère méthode 
def Affiche(request):
    projets=Projet.objects.all()
    resultat= "--".join(p.nom_projet for p in projets)
# return HttpResponse(resultat)
# syntaxe return render(request,'template',contexte)
    return render(request,'App/Affiche.html',{'projets':projets})
# 2ème méthode avec class generic
class AfficheProjet(ListView):
    model=Projet
    template_name='App/Affiche.html'
    context_object_name: "projets"
    ordering=['-nom_projet']
class DeleteProjet(DeleteView):
    model=Projet
    success_url=reverse_lazy("Aff")
class AjoutProjet(CreateView):
    model = Projet
    #1ère méthode avec fields
    #fields=["nom_projet","duree_projet","createur","temps_alouee","superviseur"]
    #fields= '__all__'
    # 2ème méthode avec forms
    form_class= AjoutForm
    success_url=reverse_lazy("Aff")


    
