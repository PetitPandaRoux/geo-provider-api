from rest_framework import serializers

from provider.models import ProviderAvailibility


class ProviderAvailibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAvailibility
        fields = [
            "provider_name",
            "gps_x_coord",
            "gps_y_coord",
            "availibility_2G",
            "availibility_3G",
            "availibility_4G",
        ]
