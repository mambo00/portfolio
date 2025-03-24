from django.contrib import admin

from skills.models import Skill


class SkillsAdmin(admin.ModelAdmin):
     list_display = ('name1', 'name2')

admin.site.register(Skill, SkillsAdmin)
