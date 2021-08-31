from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework import (generics, mixins, viewsets, filters)
from provider.models import ProviderAvailibility
from api.serializers import ProviderAvailibilitySerializer

import requests
# Create your views here.

class ProviderListView(generics.ListAPIView):
    queryset = ProviderAvailibility.objects.all()
    serializer_class = ProviderAvailibilitySerializer

def index(request):
    return HttpResponse("Hello, world. You're at api index.")