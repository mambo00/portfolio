from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from .models import Project




def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            f"Message from {name}",
            message,
            email,
            ['blessingmambo322@gmail.com'],
        )

        return HttpResponse("Message sent successfully")

    return render(request, 'index.html')