from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from django.contrib.auth.models import User

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

  operateur = models.CharField(max_length=5)
  lamb_x_coord = models.IntegerField()
  lamb_y_coord = models.IntegerField()
  gps_x_coord = models.DecimalField(max_digits=18, decimal_places=16, blank=True, null=True)
  gps_y_coord = models.DecimalField(max_digits=18, decimal_places=16, blank=True, null=True)
  index_gps_coord = models.CharField(blank=True, null=True)
  index__lamb_coord = models.CharField(blank=True, null=True)
  availibility_2G = models.BooleanField(default=False, verbose_name="2G availibility")
  availibility_3G = models.BooleanField(default=False, verbose_name="3G availibility")
  availibility_4G = models.BooleanField(default=False, verbose_name="4G availibility")

  def save(self, *args, **kwargs):
    self.index_lamb_coord = str(self.x_lamb_coord) + str(self.y_lamb_coord)
    super().save(*args, **kwargs)

  class Meta:
    indexes = [models.Index(fields=['index__lamb_coord', 'index_gps_coord']), ]
