from django.shortcuts import render, reverse, resolve_url, redirect
from django.http import HttpResponse
from django.conf import settings

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import (generics, mixins, viewsets, filters)

from provider.models import ProviderAvailibility
from api.serializers import ProviderAvailibilitySerializer

from .data_gouv_helpers import build_json_instruction, truncate, redirect_params
import requests
# Create your views here.

class ProviderListView(generics.ListAPIView):
    queryset = ProviderAvailibility.objects.all()
    serializer_class = ProviderAvailibilitySerializer


class ProviderCoordinateView(generics.ListAPIView):
  queryset = ProviderAvailibility.objects.all()
  serializer_class = ProviderAvailibilitySerializer
  def get_queryset(self):
    longitude = self.request.query_params.get('long', None)
    latitude = self.request.query_params.get('lat', None)
    return self.queryset.filter(gps_x_coord= longitude).filter(gps_y_coord=latitude)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def getAddressInfo(request):
  """
  This view call the gouvernment API to get gps long and lat of the address

  param:
    q {Str} -- address

  """
  base_url = 'https://api-adresse.data.gouv.fr/search/?q='
  string_param = request.GET.get('q', '')

  get_url = base_url + string_param

  # If not enough param has been passed, there will be too many responses from data.gouv and the request will be ban
  if(string_param):
    try:
      response = requests.get(get_url)
      response_json = response.json().get('features')
    except:
      response_json = {"error": "Something went bad calling the endpoint https://api-adresse.data.gouv.fr/search/"}
  else:
      response_json = {"error": "Please put an address as a parameter with street number, street name, postal code and city like: https://api-adresse.data.gouv.fr/search/?q=123 allée des faneurs 77185 Lognes"}

  # If more than one response, address is not precise enough, we will send back multiples possibilities
  if(len(response_json) > 1):
      current_url = request.build_absolute_uri()
      responses = build_json_instruction(current_url, response_json)
      response_json = responses
      return Response(response_json)

  longitude = truncate(response_json[0].get('geometry').get('coordinates')[0],3)
  latitude = truncate(response_json[0].get('geometry').get('coordinates')[1],3)

  params = {
    'long':longitude,
    'lat':latitude
  }
  print(params)
  return redirect_params('api-provider-items', {'long':longitude, 'lat':latitude})
  #return redirect('api-provider-items', long=longitude, lat=latitude)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def badRequests(request):
  response_json = {'error':"Something went wrong"}
  return Response(response_json)

def index(request):
    return HttpResponse("Hello, world. You're at api index.")