from django.urls import path
from wellcome import views


urlpatterns = [
    path('', views.home)
]