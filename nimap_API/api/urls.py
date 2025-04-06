from django.urls import path
from testapp import views

urlpatterns = [
    path("clients/",views.ClientAPI.as_view()),
    path("projects/",views.ProjectAPI.as_view()),

]