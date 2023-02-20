

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


