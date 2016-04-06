# Hassan Khokhar 33778724

import json
import urllib.parse
import urllib.request


MAPQUEST_API_KEY = 'd1NGPU0BWhGLfSPmVNlVuwPxYjHANOVM'                       # API Key to access MapQuest information for program

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'             # Base MapQuest URL to get the route details for program

BASE_MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1'    # Base MapQuest Elevation URL to get the elevation profile for program



def build_search_url(L: [tuple]) -> str:
    ''' This function takes a list of tuples with query parameters in them and builds
    and returns a URL that can be used to ask the MapQuest API for information about
    routes matching the search request. '''

    return BASE_MAPQUEST_URL + '/route?' + urllib.parse.urlencode(L)

    # URL is created with base MapQuest URL and Query parameters from the list of tuples




def build_elevation_url(latitude: str, longitude: str) -> str:
    ''' This function takes two strings representing a latitude and longitude of a location
    specified in a JSON Object and returns a new URL that can be used to ask the
    MapQuest API for information about the elevation profile of a certain location. '''
    
    query_parameters = [
        ('key', MAPQUEST_API_KEY), ('shapeFormat', 'raw')    # tuple representing query parameters to be put into the Elevation URL
]
    
    return BASE_MAPQUEST_ELEVATION_URL + '/profile?' + urllib.parse.urlencode(query_parameters) + '&latLngCollection=' + latitude + ',' + longitude

    # URL is created with base elevation URL, Query parameters, and latitude and longitude inputs from Route JSON Object




def get_result(url: str) -> 'json':
    ''' This function takes a URL and returns a Python object representing the
    parsed JSON response. '''

    response = None

    try:
        # Opens the URL and read the response  
        # json_text will contain the text of the (JSON format).
        
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        # Given the JSON text, we can use the json.loads() function to convert it to Python object.

        return json.loads(json_text)

    except:
        print()
        print('MAPQUEST ERROR')    # If the program is not able to read the parsed JSON response this ERROR MESSAGE will appear.

    finally:
        # Close the response when function is done no matter if opened or not.
        if response != None:
            response.close()

