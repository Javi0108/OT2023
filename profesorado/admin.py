from django.contrib import admin

from .models import Profesorado


@admin.register(Profesorado)
class ProfesoradoAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'origen', 'edad', 'description']
