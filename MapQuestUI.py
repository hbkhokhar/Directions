# Hassan Khokhar 33778724

import API_handling
import Output_handling
import time
import sys


MAPQUEST_API_KEY = 'd1NGPU0BWhGLfSPmVNlVuwPxYjHANOVM'    # API Key used to access MapQuest information for the program


def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.0225)


        

def WelcomeBanner() -> str:
    delay_print('\n*****************************************************\n')
    delay_print('******  WELCOME TO MAPQUEST CLIENT PROGRAM!!!  ******\n')
    delay_print('*****************************************************\n')
    time.sleep(1.5)
    print()
    print('Enter your directions!')
    print('----------------------')
    print()
    print('Step 1:               Enter the number of legs in route')
    print('Step 2:               Enter a valid postal code, city or other location (for each leg in the route - Press *Enter* after each location)')
    print('Step 3:               Enter the number of outputs you desire (i.e. LATLONG, STEPS, TOTALDISTANCE, TOTALTIME, ELEVATION)')
    print('Step 4:               Enter the types of output you would like printed (for each leg in the route - Press *Enter* after each location)\n')
    print('[ STEPS               Step-by-step list of directions are given for the entire route')
    print('  TOTALTIME           Total time of the entire route is given')
    print('  TOTALDISTANCE       Total distance of the entire route is given')
    print('  LATLONG             The latitude-longitude coordinates are given for each leg in the route')
    print('  ELEVATION           Elevation of each leg in the route is given (in terms of feet) ]\n')





def InputMarkers() -> [tuple]:
    ''' Function prompts a number input and a respective number of legs for
    a route and returns a list of tuples representing query paramters to be used in the URL '''
    
    LocationList = [('key', MAPQUEST_API_KEY)]           # List of query parameters where tuples are appended to

    while True:
        AmountInput = input()                            # Prompts the user for a number of locations

        if int(AmountInput) >= 2:                        # Function only works if input is at least 2 locations
            count = 0                                

            while count in range(int(AmountInput)):      # while loop goes in range of given int input
                LocationInput = input()                  # prompts for user location (valid place for MapQuest input)

                if count == 0:                           # 1st response will add 'from' and the location given to Query Parameter tuple 
                    NewTuple = ('from', LocationInput)
                    LocationList.append(NewTuple)        # it is then appended to tuples list
                    count += 1                           # add 1 to while loop

                else:
                    NewTuple = ('to', LocationInput)     # Responses after the 1st will add 'to' and location given to Query Parameter tuple  
                    LocationList.append(NewTuple)        # it is then appended to tuples list
                    count += 1                           # add 1 to while loop

            return LocationList                          # returns a list of tuples




def InputTypes() -> list:
    ''' Function prompts a number input and a respective number of command outputs for the
    function to follow and returns a list of Class Objects with command outputs to use '''
    
    OutputCommands = []                                                      # List of Output Commands to append to

    while True:
        AmountInput = input()                                                # Prompts the user for a number of command outputs 

        if int(AmountInput) >= 1:                                            # Function only works if input is at least 1 command output
            count = 0

            while count in range(int(AmountInput)):                          # while loop goes in range of given int input
                InputType = input()                                          # prompts for command outputs (i.e. ELEVATION, STEPS, etc.)

                if InputType == 'LATLONG':
                    OutputCommands.append(Output_handling.LatLongs())        # Create LatLongs() Class object for 'LATLONG' and appends to list
                    count += 1                                               # add 1 to while loop

                elif InputType == 'STEPS':                                   # Create Steps() Class object for 'STEPS' and appends to list
                    OutputCommands.append(Output_handling.Steps())           # add 1 to while loop
                    count += 1

                elif InputType == 'TOTALTIME':                               # Create TotalTime() Class object for 'TOTALTIME' and appends to list
                    OutputCommands.append(Output_handling.TotalTime())       # add 1 to while loop
                    count += 1

                elif InputType == 'TOTALDISTANCE':                           # Create TotalDistance() Class object for 'TOTALDISTANCE' and appends to list
                    OutputCommands.append(Output_handling.TotalDistance())   # add 1 to while loop
                    count += 1

                elif InputType == 'ELEVATION':                               # Create ELEVATION() Class object for 'ELEVATION' and appends to list
                    OutputCommands.append(Output_handling.Elevations())      # add 1 to while loop
                    count += 1

                else:
                    break                                                    # breaks if somehting wrong is given
                
            return OutputCommands                                            # returns the list of output command Class objects



def result(L: 'list of Classes', json_object: 'json') -> None:
    ''' Given a list of Class Objects and a Json Object for the Route API produce
    the desired result from the given output commands '''
    
    try:
        print()
        for Class in L:                                                      # iterates through the list of Class Objects
            Class.print_result(json_object)                                  # performs the desired action (example: Steps.print_result(json_result)
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')   # prints the copyright info at the end of the program
    except:
        print()                                                             # if the function doesn't work...
        print('NO ROUTE FOUND\n')                                           # print this ERROR MESSAGE
        

            

def MapQuest_user_interface() -> None:
    ''' Acts as the user interface for the MapQuest Program '''

    WelcomeBanner()
    Markers = InputMarkers()                                                            # Calls the InputMarkers() function
    JsonObjectRoute = API_handling.get_result(API_handling.build_search_url(Markers))   # Markers gets taken in as a parameter to this nested functions to create the JSON Object from the Route API
    OutputList = InputTypes()                                                           # Calls to the InputTypes()
    Final = result(OutputList, JsonObjectRoute)                                         # OutputList and previous Json Object are taken to produce the final Result

    while True:                                                                         # when program ends, don't exit... just keep it in a loop
        time.sleep(1)


        

if __name__ == '__main__':
    MapQuest_user_interface()   # Module executes the user interface function to start the program



