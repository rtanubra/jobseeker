from django.shortcuts import render,get_object_or_404
from .models import Job
from .forms import JobChangeForm
from datetime import date
from dateutil.relativedelta import relativedelta

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
# Create your views here.
class JobListView(ListView):
    #Next three lines used to filter dates
    today = date.today()
    last_month = today - relativedelta(months=1)
    queryset = Job.objects.filter(job_last_action__range=[last_month,today])
    #queryset = Job.objects.all()

class JobListView2(ListView):
    queryset= Job.objects.filter(job_qualified__gt=-1)

class JobDetailView(DetailView):
    template_name = 'jobs/job_detail.html'
    queryset= Job.objects.all()

class JobUpdateView(UpdateView):
    template_name= 'jobs/job_update.html'
    queryset= Job.objects.all()
    form_class = JobChangeForm