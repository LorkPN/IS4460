from django.urls import path
from .views import CustomerListView, CustomerListCreateView, CustomerDetailView


urlpatterns = [
    path('list/',CustomerListView.as_view(),name='customer-list'),
    path('api/', CustomerListCreateView.as_view(), name='customer-list-view'),
    path('api/<int:pk>', CustomerDetailView.as_view(), name='customer-detail-view'),
]