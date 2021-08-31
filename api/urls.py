from django.urls import path
from .views import(ProviderListView)

from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('providers/address/',view.getAddressInfo, name='api-get-address' ),
    path('providers', ProviderListView.as_view(), name='api-provider-list')
]