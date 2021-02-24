from django.urls import path

from .views import RentalPropertyListView

urlpatterns = [
    path('', RentalPropertyListView.as_view()),
]