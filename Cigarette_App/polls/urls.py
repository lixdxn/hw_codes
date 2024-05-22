from django.urls import path
from .views import CigaretteListView, CigaretteDetailView

urlpatterns = [
    path('', CigaretteListView.as_view(), name='cigarette_list'),
    path('cigarette/<int:pk>/', CigaretteDetailView.as_view(), name='cigarette_detail'),
]