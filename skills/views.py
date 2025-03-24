from django.shortcuts import render

from .models import Skill


def skill(request):
    skills = Skill.object.all()
    return render(request, 'index.html', {'skill': skills})
