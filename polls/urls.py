from django.urls import path

from .views.rental_property import RentalPropertyListView
from .views.rental_property_saved import RentalPropertySavedListView

app_name = 'main'

urlpatterns = [
    path('', RentalPropertyListView.as_view()),
    path('saved', RentalPropertySavedListView.as_view()),
    path('promote/<int:pk>', RentalPropertyListView.promote, name="promote"),
    path('destroy/<int:pk>', RentalPropertyListView.destroy, name="destroy"),
    path('block/<int:pk>', RentalPropertyListView.black_list, name="block"),
]