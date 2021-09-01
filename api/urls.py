from django.urls import path
from .views import ProviderListView, ProviderCoordinateView

from . import views


urlpatterns = [
    path("address/", views.get_addres_info, name="api-get-address"),
    path("providers/", ProviderListView.as_view(), name="api-provider-list-all"),
    path(
        "provider/coordinate/",
        ProviderCoordinateView.as_view(),
        name="api-provider-items",
    ),
    path("failed-endpoint/", views.end_point_failed, name="api-failed-endpoint"),
]
