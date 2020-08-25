from django.shortcuts import render
from .models import Job

def home(request):
	jobs = Job.objects    #It will call all the objects in the job database
	return render(request, 'jobs/home.html', {'jobs':jobs})
