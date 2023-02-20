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
    
    def __init__(self, n_rooms):
        self.__planet = ["None"] * n_rooms
        self.__n_rooms = n_rooms
        
    def initialize(self):
        animal_types = [Bear, Fish, "None"]
        self.__planet = [animal_type(i) if animal_type != "None" else "None" for i, animal_type in enumerate(np.random.choice(animal_types, size=self.__n_rooms))]
    
    def next_time_step(self, n_steps=1, print_result=True):
        self.__n_rooms = max(self.__n_rooms, n_steps) 
        for i in range(n_steps):
            room_to_move = np.random.choice(list(range(self.__n_rooms)))
            if self.__planet[room_to_move] == "None":
                pass
            else:
                animal = self.__planet[room_to_move]
                new_room = animal.move(self.__planet)
                if not (0 <= new_room < len(self.__planet)):
                    continue
                if animal.__class__.__name__ == "Bear":
                    if self.__planet[new_room].__class__.__name__ == "Bear":
                        pass
                    elif self.__planet[new_room].__class__.__name__ == "Fish":
                        self.__planet[new_room] = Bear(new_room)
                        self.__planet[room_to_move] = "None"
                    else:
                        self.__planet[new_room] = Bear(new_room)
                elif animal.__class__.__name__ == "Fish":
                    if self.__planet[new_room].__class__.__name__ == "Fish":
                        pass
                    elif self.__planet[new_room].__class__.__name__ == "Bear":
                        self.__planet[room_to_move] = "None"
                    else:
                        self.__planet[new_room] = Fish(new_room)
                if print_result:
                    print(f"{animal} in place {room_to_move} moved to {new_room} place.")
        
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