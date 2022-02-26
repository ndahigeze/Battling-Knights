from typing import List

LIFE_STATUS=("ALIVE","DEAD","DROWNED")

class Knight:
    def __init__(
            self,
            id,
            position, #[row,col]
            status,
            items,
            base_attack,
            base_defense
         ):
        self.id=id
        self.position:position
        self.status=status
        self.items=items
        self.base_attack=base_attack
        self.base_defense=base_defense


    def move(self,direction):
        if direction == "S":  # DOWN
            self.position = [self.position[0]+1, self.position[1]]  # add one to row
        elif direction == "N":  # UP
            self.position = [self.position[0]-1, self.position[1]]  # reduce one to row
        elif direction == "W":  # LEFT
            self.position = [self.position[0], self.position[1]-1]  # reduce one to column
        elif direction == "E":  # RIGHT
            self.position = [self.position[0], self.position[1]+1]  # add one to column












