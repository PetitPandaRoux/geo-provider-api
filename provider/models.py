from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from django.contrib.auth.models import User
from .coord_converter import convert_lambert93_to_gps

# Create your models here.
class DateModification(models.Model):
  """
  An abstract class to handle creation date and modification date 
  """
  creation_date = models.DateTimeField(auto_now_add=True)
  last_modification_date = models.DateTimeField(auto_now=True)

  class Meta:
      abstract = True


PROVIDER_CODE_NAME = (
  ('20801', 'Orange'),
  ('20810', 'SFR'),
  ('20815', 'FREE'),
  ('20820', 'Bouygues')
)

class ProviderAvailibility(DateModification):
  """
  Availibility of a provider connexion given a coordinate
  """

  provider_code = models.CharField(max_length=5)
  provider_name = models.CharField(max_length=255, blank=True, null=True)
  lamb_x_coord = models.IntegerField()
  lamb_y_coord = models.IntegerField()
  # For gps coordinate we only take 3 decimal place, it gives an approximation of around 100 meters
  # More informations https://wiki.gis.com/wiki/index.php/Decimal_degrees
  gps_x_coord = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
  gps_y_coord = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
  index_lamb_coord = models.CharField(max_length=255, blank=True, null=True)
  availibility_2G = models.BooleanField(default=False, verbose_name="2G availibility")
  availibility_3G = models.BooleanField(default=False, verbose_name="3G availibility")
  availibility_4G = models.BooleanField(default=False, verbose_name="4G availibility")

  def save(self, *args, **kwargs):
    # Fill gps coordinate if needed
    if(not self.gps_x_coord or not self.gps_y_coord):
      point = convert_lambert93_to_gps(self.lamb_x_coord, self.lamb_y_coord)
      self.gps_x_coord = point.long
      self.gps_y_coord = point.lat
    
    self.provider_name = dict(PROVIDER_CODE_NAME).get(self.provider_code)

    # Create id to accelerate queries to databases
    self.index_lamb_coord = str(self.lamb_x_coord) + str(self.lamb_y_coord)
    super().save(*args, **kwargs)

  class Meta:
    indexes = [models.Index(fields=['index_lamb_coord', ]), ]
