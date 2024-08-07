from django.urls import path
from .views import BookingListAPI

urlpatterns = [
    path('', BookingListAPI.as_view()),
]
