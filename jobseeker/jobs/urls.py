from django.urls import path
from .views import (
    JobListView,
    JobUpdateView,
)

app_name="jobs"

urlpatterns = [
    path("",JobListView.as_view(),name="jobs_list"),
    path("<int:job_id>/update/",JobUpdateView.as_view(), name='jobs_update')
]
