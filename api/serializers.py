from rest_framework import serializers 

from provider.models import ProviderAvailibility

class ProviderAvailibilitySerializer(serializers.ModelSerializer):

  class Meta:
    model = ProviderAvailibility
    fields = "__all__"