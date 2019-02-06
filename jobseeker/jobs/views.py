from django.shortcuts import render
from .models import Job

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
    queryset = Job.objects.all()
