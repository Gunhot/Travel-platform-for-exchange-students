from django.urls import path, include
from .views import *
urlpatterns = [
    path('', TripList.as_view()),
    path('<int:pk>/', TripDetail.as_view()),
    path('filter/', filter)
]
