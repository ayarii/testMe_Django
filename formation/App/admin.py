from django.contrib import admin
from App.models import *
# Register your models here.
class MemberShip(admin.TabularInline):
    model = memberShipInProject
    extra = 0
class SearchEtudiant(admin.ModelAdmin):
    search_fields=['nom']
@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display=('nom_projet','duree_projet','etat','temps_alouee','createur','superviseur')
    fieldsets=(
       ('Apropos',{'fields':('nom_projet','etat')}),
       ('Durée',{'fields':('duree_projet','temps_alouee')}),
       (None,{'fields':('createur','superviseur')})
    )
    inlines = (MemberShip,)
    autocomplete_fields=["createur"]
    list_per_page=1
    list_filter=('etat','createur')
#activer le model dans le dashboard Admin
admin.site.register(Etudiant,SearchEtudiant)
#admin.site.register(Projet,ProjetAdmin)
admin.site.register(coach)