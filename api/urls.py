from django.urls import path
from .views import(ProviderListView, ProviderCoordinateView)

from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('address/',views.getAddressInfo, name='api-get-address' ),
    path('providers/', ProviderListView.as_view(), name='api-provider-list-all'),
    path('provider/coordinate/', ProviderCoordinateView.as_view(), name='api-provider-items')
]