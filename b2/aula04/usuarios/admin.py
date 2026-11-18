from django.contrib import admin
from django.contrib.admin.decorators import display
from . models import Usuario


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email',)
    search_fields = ('nome', 'email',)
    readonly_fields = ('senha',)
