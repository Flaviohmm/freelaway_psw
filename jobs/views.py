from django.shortcuts import render
from .models import Jobs
# Create your views here.


def encontrar_jobs(request):
    if request.method == "GET":
        jobs = Jobs.objects.filter(reservado=False)
        return render(request, 'encontrar_jobs.html', {'jobs': jobs})
