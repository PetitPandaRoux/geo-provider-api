import pyproj
from collections import namedtuple 

def convert_lambert_to_gps(x: int, y: int) -> tuple:
  """
  It returns a named tuple of gps coordinate from lambert93 coordinate
  """
  lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
  wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
  
  #We want to return a namedtuple -> easier to manipulate
  gps_coordinate = namedtuple('Point', 'x y')
 
  #We force type casting for x and y to int
  lon, lat = pyproj.transform(lambert, wgs84, int(x), int(y))
  point = gps_coordinate(lon, lat)

  return point

