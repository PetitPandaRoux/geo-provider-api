from django.test import TestCase
from .coord_converter import convert_lambert93_to_gps, convert_gps_to_lambert93
from .models import ProviderAvailibility
from decimal import Decimal

# Create your tests here.
class CoordConverterTestCase(TestCase):
  
  def test_coordinate_should_return_valid_gps(self):
    """Function should return expected gps coordinates"""

    # GIVEN
    x = 102980
    y = 6847973

    #EXPECTED
    expected_long = -5.0888561153013425
    expected_lat = 48.4565745588153

    result = convert_lambert93_to_gps(x, y)
    self.assertEqual(result.long, expected_long)
    self.assertEqual(result.lat, expected_lat)

  def test_coordinate_should_return_valid_gps_given_string(self):
    """Function should return expected gps coordinate when given string as parameters"""

    # GIVEN
    x = "103113"
    y = "6848661"

    #EXPECTED
    expected_long = -5.088018169414728
    expected_lat = 48.46285384827896

    result = convert_lambert93_to_gps(x, y)

    self.assertEqual(result.long, expected_long)
    self.assertEqual(result.lat, expected_lat)

class ProviderAvailibilityTestCase(TestCase):

  def test_index_and_gps_coord_should_be_created(self):
    """index_lamb_coord should be concatenation of x and y lambert 93 coordinates"""
        #From csv provided 20810;103113;6848661;1;1;0
    ProviderAvailibility.objects.create(
      provider_code='20810',
      lamb_x_coord=103113,
      lamb_y_coord=6848661,
      availibility_2G=True,
      availibility_3G=True,
      availibility_4G=False)
  
    coord = ProviderAvailibility.objects.get(index_lamb_coord='1031136848661')

    self.assertEqual(coord.index_lamb_coord, '1031136848661')

    #We use almost equal to workaround truncating and rounding
    self.assertAlmostEqual(coord.gps_x_coord, Decimal(-5.088018169414728))
    self.assertAlmostEqual(coord.gps_y_coord, Decimal(48.46285384827896))

  def test_same_index_should_return_2_rows(self):
    """We test the case when two rows have same index but different operators"""
    ProviderAvailibility.objects.create(
      provider_code='20810',
      lamb_x_coord=103113,
      lamb_y_coord=6848661,
      availibility_2G=True,
      availibility_3G=True,
      availibility_4G=False)

    ProviderAvailibility.objects.create(
      provider_code='20815',
      lamb_x_coord=103113,
      lamb_y_coord=6848661,
      availibility_2G=False,
      availibility_3G=False,
      availibility_4G=False)

    coord = ProviderAvailibility.objects.all().filter(index_lamb_coord='1031136848661')
    self.assertEqual(coord[0].provider_code, '20810')
    self.assertEqual(coord[1].provider_code, '20815')
