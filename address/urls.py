from django.urls import path
from .views import AddressView, AddressesView, PostalView

urlpatterns = [
    path('address', AddressesView.as_view()),
    path('address/<str:address_id>', AddressView.as_view()),
    path('postalcodes', PostalView.as_view()),
]
