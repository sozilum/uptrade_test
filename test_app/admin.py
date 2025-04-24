from django.contrib import admin
from .models import (Menu,
                     InnerMenu,
                     )

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(InnerMenu)
class InnerMenuAdmin(admin.ModelAdmin):
    list_display = [
        'menu',
        'name',
        'url',
        'innerurl',
    ]

    list_filter = [
        'menu',
    ]