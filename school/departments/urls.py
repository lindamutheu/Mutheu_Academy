from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentsListCreate.as_view(), name="students-view-create"),
    path("students/<int:pk>/", views.StudentsRetrieveUpdateDestroy.as_view(), name="update"),
]
