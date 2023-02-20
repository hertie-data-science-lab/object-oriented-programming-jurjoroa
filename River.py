import numpy as np

from Creature import Bear
from Creature import Fish

class River:
    
    def __init__(self, n_room):
        self.__planet = "None"
        self.__n_room = n_room
        
    
    def initialize(self):
        animals = np.random.choice([Bear, Fish, "None"], size = self.__n_room) #Assign three types
        self.__planet = []

        for place, types in enumerate(animals): #Enumerate help us to iterate through our options according to the index.
            self.__planet.append(types(place) if types != "None" else "None")
    
    def next_time_step(self, n = 1, print_result = True):
        self.__n_room = max(self.__n_room, n) 
        for i in range(n):
            place_move = np.random.choice(list(range(self.__n_room)))
            if self.__planet[place_move] == "None": #If types is equal to "None", it's added to __planet list.
                pass
            else:
                types = self.__planet[place_move]
                new_range = types.move( self.__planet)

                if new_range < 0 or new_range > len( self.__planet) - 1:
                    pass

                else:

                    if isinstance(types, Bear):
                        if isinstance( self.__planet[new_range], Bear):

                            pass

                        elif isinstance( self.__planet[new_range], Fish):

                            self.__planet[new_range] = Bear(new_range)
                            self.__planet[place_move] = "None"

                        else:
                            self.__planet[new_range] = Bear(new_range)

                    elif isinstance(types, Fish):

                        if isinstance( self.__planet[new_range], Fish):
                            pass

                        elif isinstance( self.__planet[new_range], Bear):
                            self.__planet[place_move] = "None"

                        else:
                            self.__planet[new_range] = Fish(new_range)

                if print_result == True:
                    print(f"{types} {place_move} -> to {new_range} place")
        
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.__planet, "\n")
        print("===================")

