from django.shortcuts import render, reverse, resolve_url, redirect
from django.http import HttpResponse
from django.conf import settings

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics

from provider.models import ProviderAvailibility
from api.serializers import ProviderAvailibilitySerializer

from .data_gouv_helpers import (
    manage_multiple_address_reponses,
    truncate,
    redirect_params,
)
import requests


class ProviderListView(generics.ListAPIView):
    """This is a view used test"""

    queryset = ProviderAvailibility.objects.all()[:5]
    serializer_class = ProviderAvailibilitySerializer


class ProviderCoordinateView(generics.ListAPIView):
    """
    This view generate information on provider availibility on given long and lat coordinate

    params:
      long {Float} -- Longitude
      lat {Float}  -- Latitude
    """

    queryset = ProviderAvailibility.objects.all()
    serializer_class = ProviderAvailibilitySerializer

    def get_queryset(self):
        longitude = self.request.query_params.get("long", None)
        latitude = self.request.query_params.get("lat", None)
        return self.queryset.filter(gps_x_coord=longitude).filter(gps_y_coord=latitude)


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def end_point_failed(request):
    error_json = request.GET.get("error", "")
    return Response(error_json)


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def get_addres_info(request):
    """
    This view call the gouvernment API to get gps long and lat of the address

    param:
      q {Str} -- address

    """
    base_url = "https://api-adresse.data.gouv.fr/search/?q="
    string_param = request.GET.get("q", "")

    get_url = base_url + string_param

    # If not enough param has been passed, there will be too many responses from data.gouv and the request will be ban
    if string_param:
        try:
            response = requests.get(get_url)
            response_json = response.json()
        except:
            response_json = {
                "error": "Something went bad calling the endpoint https://api-adresse.data.gouv.fr/search/"
            }

    else:
        return redirect_params(
            "api-failed-endpoint",
            {
                "error": "Please put an address as a parameter with street number, street name, postal code and city like: https://api-adresse.data.gouv.fr/search/?q=123 allée des faneurs 77185 Lognes"
            },
        )

    #  api-adresse.data.gouv.fr send an empty features when too many possibilities arise
    if len(response_json.get("features")) == 0:
        return redirect_params(
            "api-failed-endpoint",
            {"error": "Your address is not precise enough, too many possibilities"},
        )

    # api-adresse.data.gouv.fr can send back multiples possibilities if search is narrow enough
    if len(response_json.get("features")) > 1:
        current_url = request.build_absolute_uri()
        responses = manage_multiple_address_reponses(
            current_url, response_json.get("features")
        )
        return Response(responses)

    response_json = response_json.get("features")
    longitude = truncate(response_json[0].get("geometry").get("coordinates")[0], 3)
    latitude = truncate(response_json[0].get("geometry").get("coordinates")[1], 3)

    params = {"long": longitude, "lat": latitude}

    return redirect_params("api-provider-items", {"long": longitude, "lat": latitude})
    # return redirect('api-provider-items', long=longitude, lat=latitude)
