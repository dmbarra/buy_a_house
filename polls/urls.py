from django.urls import path

from .views import RentalPropertyListView

app_name = 'main'

urlpatterns = [
    path('', RentalPropertyListView.as_view()),
    path('destroy/<int:pk>', RentalPropertyListView.destroy, name="destroy"),
    path('block/<int:pk>', RentalPropertyListView.black_list, name="block"),
]