from django.contrib import admin
from contato import models

# Register your models here.
@admin.register(models.Contato)
class ContatoAdmin(admin.ModelAdmin):
    ...