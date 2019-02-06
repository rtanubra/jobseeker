from django.db import models
from datetime import date

# Create your models here.
class Job(models.Model):

    def __str__(self):
        return self.job_company[:20]+" "+self.job_title[:20]

    job_title = models.CharField(max_length=100)
    job_company = models.CharField(max_length=100)
    job_link = models.CharField(max_length=300)
    job_applied = models.BooleanField(default=False)
    #Need to figure out how to limit from -1,0,1
    job_qualified = models.IntegerField(default=0)
    #Need to limit this from -1(rejected),0,1,2,
    job_application_status = models.IntegerField(default=0)
    job_last_action = models.DateField()
    job_comment = models.TextField(default="Job Pulled, let's apply")
