from django.shortcuts import render,HttpResponse,redirect
from App.models import *
from django.views.generic import *
from django.urls import reverse_lazy
from .forms import AjoutForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return HttpResponse("Bonjour Asma")
def home(request,up):
#return HttpResponse("Bonjour "+up)
    return HttpResponse(f"Bonjour UP{up}")
# 1ère méthode 
@login_required(login_url="login")
def Affiche(request):
    projets=Projet.objects.all()
    resultat= "--".join(p.nom_projet for p in projets)
# return HttpResponse(resultat)
# syntaxe return render(request,'template',contexte)
    return render(request,'App/Affiche.html',{'projets':projets})
# 2ème méthode avec class generic
class AfficheProjet(LoginRequiredMixin,ListView):
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
class UpdateProjet(UpdateView):
    model=Projet
    form_class= AjoutForm 
    success_url=reverse_lazy("Aff")  
# login
def loginUser(request):
    if request.method=="POST":
        name=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('Aff')
        else:
            messages.info(request,'username ou password invalide ')
            return redirect('login')
    else: 
        return render(request,'App/login.html')
