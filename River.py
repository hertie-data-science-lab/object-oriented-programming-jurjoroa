import numpy as np

from Creature import Bear
from Creature import Fish

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
                    print(f"{animal} in [{room_to_move}] -> {new_room} place.")
        
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.__planet, "\n")
        print("===================")


