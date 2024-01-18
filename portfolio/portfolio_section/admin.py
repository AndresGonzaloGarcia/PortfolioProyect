from django.contrib import admin
from .models import Project

#habilita la posibilidad de ver estos campos en la seccion de agregar proyecto
class Project_admin(admin.ModelAdmin):
    readonly_fields= ('created_at', 'updated_at')



admin.site.register(Project, Project_admin)

