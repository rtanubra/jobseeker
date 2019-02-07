from django import forms
from .models import Job

class JobChangeForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "job_applied",
            'job_qualified',
            'job_application_status',
            'job_last_action',
            'job_comment'
        ]