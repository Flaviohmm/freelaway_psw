from django.shortcuts import render

# Create your views here.


def encontrar_jobs(request):
    return render(request, 'encontrar_jobs.html')
