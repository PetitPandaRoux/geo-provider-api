from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework import (generics, mixins, viewsets, filters)

from provider.models import ProviderAvailibility
from api.serializers import ProviderAvailibilitySerializer

import requests
# Create your views here.

class ProviderListView(generics.ListAPIView):
    queryset = ProviderAvailibility.objects.all()
    serializer_class = ProviderAvailibilitySerializer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def getAddressInfo(request):
    response = requests.get('https://api.radioking.io/widget/radio/radio-raptz/track/current')
    current_show = response.json()
    return Response(current_show)

def index(request):
    return HttpResponse("Hello, world. You're at api index.")