from django.shortcuts import render,get_object_or_404
from .models import Job
from .forms import JobChangeForm

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

class JobUpdateView(UpdateView):
    queryset = Job.objects.all()
    template_name = 'jobs/job_update.html'
    fields = [
        "job_applied",
        'job_qualified',
        'job_application_status',
        'job_last_action',
        'job_comment'
    ]
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        job_id = self.kwargs.get('job_id')
        job = get_object_or_404(Job,id=job_id)
        context["job"] = job
        return context

    def get_object(self):
        id = self.kwargs.get('job_id')

