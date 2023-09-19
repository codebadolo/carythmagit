from django.contrib import admin
from  .models import Testme , DonneeECG , Client


admin.site.register(Testme)
admin.site.register(DonneeECG)


class ClientAdmin(admin.ModelAdmin):
     list_display = ('phone', 'date_naissance', 'is_staff')  # Champs à afficher dans la liste
     list_filter = ('is_staff', 'is_superuser')  # Filtres sur le côté droit
     search_fields = ('phone', 'first_name', 'last_name')  # Barre de recherche

admin.site.register(Client , ClientAdmin)
