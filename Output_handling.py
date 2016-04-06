# Hassan Khokhar 33778724

import API_handling
import math
import MapQuestUI



class LatLongs:   # CLASS OBJECT WHICH REPRESENTS THE OUTPUT COMMAND FOR 'LATLONG'

    def print_result(self, json_object: 'json') -> None:
        ''' This function takes a parsed JSON response from the MapQuest API's
        search request and prints the latitude and longitude of all the locations
        specified in the input. '''

        JsonObject = json_object['route']['locations']     # filter through JSON Object to get desired field
        print('LATLONGS')
        for route in JsonObject:                           # iterate through the JSON Object... 
            print(format(route['latLng']['lat'], '.2f'), 'N', format(route['latLng']['lng'], '.2f'), 'W')   # print the desired latitude and longitude (rounded with direction header - all valid locations are ALWAYS N & W according to world map)
        print()




class Steps:      # CLASS OBJECT WHICH REPRESENTS THE OUTPUT COMMAND FOR 'STEPS'

    def print_result(self, json_object: 'json') -> None:
        ''' This function takes a parsed JSON response from the MapQuest API's
        search request and prints the directions to all the legs of the route in sequential order '''

        JsonObject = json_object['route']['legs']         # filter through JSON Object to get desired field
        print('DIRECTIONS')       
        for route in JsonObject:                          # iterate through the JSON Object... 
            for dictionary in route['maneuvers']:         
                print(dictionary['narrative'])            # prints each step of the route in order
        print()




class TotalTime:    # CLASS OBJECT WHICH REPRESENTS THE OUTPUT COMMAND FOR 'TOTALTIME'

    def print_result(self, json_object: 'json') -> None:
        ''' This function takes a parsed JSON response from the MapQuest API's
        search request and prints the total time it takes to complete the route '''
        
        print('TOTAL TIME: ', math.ceil(json_object['route']['time']/60), 'minutes')   # filters through JSON Object and prints the total time rounded to minutes
        print()





class TotalDistance:     # CLASS OBJECT WHICH REPRESENTS THE OUTPUT COMMAND FOR 'TOTALDISTANCE'
    
    def print_result(self, json_object: 'json') -> None:
        ''' This function takes a parsed JSON response from the MapQuest API's
        search request and prints the total distance of the entire route. '''

        print('TOTAL DISTANCE: ', math.ceil(json_object['route']['distance']), 'miles')  # filters through JSON Object and prints the total distance in miles
        print()




class Elevations:        # CLASS OBJECT WHICH REPRESENTS THE OUTPUT COMMAND FOR 'ELEVATIONS'
    
    def print_result(self, json_object: 'json') -> None:
        ''' This function takes a parsed JSON response from the MapQuest API's
        search request and prints the elevations of each location in the input. '''

        JsonObject = json_object['route']['locations']       # filters through JSON Object....

        print('ELEVATIONS')

        for route in JsonObject:                            # iterate through the JSON Object... 
            elevationURL = API_handling.build_elevation_url(str(route['latLng']['lat']) , str(route['latLng']['lng']))   # nested function create the elevation URL from the latitude and longitude from the JSON Object input
            JsonObjectElevation = API_handling.get_result(elevationURL)  # Creates a new JSON Object representing the Elevation Profile

            for elevation in JsonObjectElevation['elevationProfile']:    # iterate through the JSON ELEVATION Object... 
                print(elevation['height'])                               # prints the elevation of each location given
        print()

