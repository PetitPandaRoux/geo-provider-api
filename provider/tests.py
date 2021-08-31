from django.test import TestCase
from .coord_converter import convert_lambert93_to_gps


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
    x = "102980"
    y = "6847973"

    #EXPECTED
    expected_long = -5.0888561153013425
    expected_lat = 48.4565745588153

    result = convert_lambert93_to_gps(x, y)
    self.assertEqual(result.long, expected_long)
    self.assertEqual(result.lat, expected_lat)
