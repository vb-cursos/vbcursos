from django.contrib import admin
from .models import *

# Register your models here.
# from sitealto.core.models import About, Service, RecentWork, Client, Feedbacks

"""
admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Feedbacks)
"""

class ModuloInline(admin.TabularInline):
    model = Modulo
    extra = 0

class CursoAdmin(admin.ModelAdmin):
    inlines = [ModuloInline]

admin.site.register(Curso, CursoAdmin)
admin.site.register(FaqGeral)
admin.site.register(Feedbacks)