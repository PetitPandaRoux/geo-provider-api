from django.test import TestCase
from .coord_converter import convert_lambert_to_gps
from .models import ProviderAvailibility

# Create your tests here.
class CoordConverterTestCase(TestCase):

  def test_coordinate_should_return_valid_gps(self):
    """Function should return expected gps coordinate"""

    # GIVEN
    x = 102980
    y = 6847973

    #EXPECTED
    expected_x = -5.0888561153013425
    expected_y = 48.4565745588153

    result = convert_lambert_to_gps(x, y)
    self.assertEqual(result.x, expected_x)
    self.assertEqual(result.y, expected_y)

  def test_coordinate_should_return_valid_gps_given_string(self):
    """Function should return expected gps coordinate when given string as parameters"""

    # GIVEN
    x = "102980"
    y = "6847973"

    #EXPECTED
    expected_x = -5.0888561153013425
    expected_y = 48.4565745588153

    result = convert_lambert_to_gps(x, y)
    self.assertEqual(result.x, expected_x)
    self.assertEqual(result.y, expected_y)