from django.urls import path
from .views import (
    JobListView,
    JobListView2,
    JobUpdateView,
    JobDetailView,
)

app_name="jobs"

urlpatterns = [
    path("",JobListView.as_view(),name="jobs_list"),
    path("q/",JobListView2.as_view(),name='jobs_list'),
    path("<int:pk>/",JobDetailView.as_view(),name='jobs_detail'),
    path("<int:pk>/update/",JobUpdateView.as_view(), name='jobs_update'),
]
