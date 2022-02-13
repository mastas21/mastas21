

from urllib import request, response
import requests
import constants
from shapely.geometry import shape, Point



def fct():
    response = requests.get(constants.BASE)
    dict=response.json()
# construct point based on lon/lat returned by geocoder
    point = Point( -73.6062391 , 45.5973446)
# check each polygon to see if it contains the point
    for feature in dict['features']:
        
        polygon = shape(feature['geometry'])
    
        if polygon.contains(point):
            print ('Found containing polygon:', feature)
            break
    

fct()
