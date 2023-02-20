#1.- First, we import our ABCMEta to use our abstract method.

from abc import ABCMeta, abstractmethod


#2.- We create our Creature with our two classes: Bears and Fishs

class Creature:
    pass

class Bear:
    pass

class Fish:
    pass


import numpy as np
from abc import ABC, abstractmethod

#Creatures

class Creature(ABC):
    def __init__(self, place):
        self.place = place
        self.animal = None

    @abstractmethod #We defined the abstract method for apply the movements to all the animals or creatures
    def move(self, planet):
        pass

    def __repr__(self):
        return self.animal


class Bear(Creature):
    def __init__(self, place):
        super().__init__(place) #Super() help us to for reference of the base class (according to the web)
        self.animal = "B"

    def move(self, planet):
        neigh = [i for i in range(len(planet)) if i != self.place]
        z_index = np.random.choice(neigh)
        return z_index


class Fish(Creature):
    def __init__(self, place):
        super().__init__(place)  #Super() help us to for reference of the base class (according to the web). Also for Fish
        self.animal = "F"

    def move(self, planet):
        neigh = [i for i in range(len(planet)) if i != self.place] #List of all our positions--index
        empty_neighbors = [i for i in neigh if not planet[i]]
        if empty_neighbors: #If there are no empty positions, Bear or Fish moves randomly 
            z_index = random.choice(empty_neighbors)
        else:
            z_index = random.choice(neigh)
        return z_index

#River

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

                #Here we ignore if the animals moved outside the boundaries of the list. 
                if new_range < 0 or new_range > len( self.__planet) - 1:
                    pass

                else:

                    if isinstance(types, Bear):
                        if isinstance( self.__planet[new_range], Bear):
                            #If the creature in the new position is also a Bear, nothing happens, and the bear stays in its current position.

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






river = River(10)
river.initialize()
river.display()

river.next_time_step(10)

river.display()