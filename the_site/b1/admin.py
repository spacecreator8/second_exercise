from django.contrib import admin
from .models import *


admin.site.register(User)

admin.site.register(Category)
admin.site.register(Realization)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_creation')
    list_display_links = ('id','name')
    ordering = ['date_creation']

admin.site.register(Application, ApplicationAdmin)

