from django.contrib import admin

from skills.models import Skill
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'languages')




admin.site.register(Project, ProjectAdmin)

