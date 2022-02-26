
class Play:
    items = ["A", "M", "D", 'H']
    nights = ["R", "Y", "B", "G"]

    items_priorities = {
        "A": 1,
        "M": 2,
        "D": 3,
        "H": 4
    }


    @staticmethod
    def find_location(direction, current_location):
        """
         Findig the location where the night will move to
        :param direction:
        :param current_location:
        :return:
        """
        # print(current_location)
        if direction == "S":  # DOWN
            return [current_location[0]+1, current_location[1]]  # add one to row
        elif direction == "N":  # UP
            return [current_location[0]-1, current_location[1]]  # reduce one to row
        elif direction == "W":  # LEFT
            return [current_location[0], current_location[1]-1]  # reduce one to column
        elif direction == "E":  # RIGHT
            return [current_location[0], current_location[1]+1]  # add one to column

    def get_best_item(self, location, board):
        """
        Check if the location has any item and return the highest priority item if items on location are more than one
        :param location:
        :param board:
        :return:
        """

        found_items = {
            "counter": 0,
            "key": ""
        }
        prev = ""

        for item in self.items:
            if location == board[item][0]:

                if len(prev) > 0:
                    if self.items_priorities[item] > self.items_priorities[prev]:
                        found_items["counter"] = found_items["counter"] + 1
                        found_items["key"] = item
                else:
                    found_items["counter"] = found_items["counter"] + 1
                    found_items["key"] = item




                prev = item

        return found_items

    @staticmethod
    def find_item_value(item):

        """
         Find the value of the item a night is acquired
        :param item:
        :return:
        """
        i_value={
            'attack':0,
            'defense':0,
        }
        if item == "A":
            i_value["attack"]=2
        elif item == "D":
            i_value["attack"] = 1
        elif item == "H":
            i_value["defense"] = 1
        elif item == "M":
            i_value["attack"] = 1
            i_value["defense"] = 1

        return i_value

    def check_another_night(self, location, board):

        """
        Check if there is another night to the new location
        :param location:
        :param boad:
        :return:
        """
        night = {
            "found": False,
            "key": ""
        }
        for n in self.nights:
            if location == board[n][0]:
                night["found"] = True
                night["key"] = n
                return night
        return night

    @staticmethod
    def fight(attacker,defender,location):
        """
        This where the two nights fight
        :param attacker:
        :param defender:
        :param location:
        :return:
        """
        attacker_score = 0
        defender_score = 0

        loser_item = ""
        attacker_score = 0.5+attacker[3]
        defender_score = defender[4]
        if attacker_score > defender_score:
            attacker[1]="LIVE"
            attacker[0]=location

            defender[1] = "DEAD"
            defender[0] = [-1,-1]
            defender[3] = 0
            defender[4] = 0
            loser_item = defender[2]
            defender[2]=None
        else:
            attacker[1] = "DEAD"
            attacker[0] = [-1,-1]
            attacker[3] = 0
            attacker[4] =0
            loser_item = attacker[2]
            attacker[2]=None
            defender[1] = "LIVE"

        result = {
            "attacker": attacker,
            "defender": defender,
            "loser_item": loser_item,

        }
        return result

    def acquire_item(self,board,location,item,night):
        """
         Acquire item on the tile
        :param board:
        :param location:
        :param item:
        :param night:
        :return:
        """
        print(location)
        board[night][2] = item["key"]
        board[item["key"]][0] = location
        board[item["key"]][1] = True
        item_value = self.find_item_value(item["key"])
        board[night][3] = board[night][3] + item_value["attack"]
        board[night][4] = board[night][4] + item_value["defense"]
        return board

    def move(self,night_move,board):
        """
         Handling moving the nights
        :param night_move:
        :param board:
        :return:
        """
        night = night_move[0]
        current_location = board[night][0]
        direction = night_move[1]
        new_location = ""
        if 0 <= current_location[0] <= 8 and 0 <= current_location[1] <= 8:
            new_location = self.find_location(direction, current_location)
        item_found = self.get_best_item(new_location, board)
        defender = self.check_another_night(new_location, board)

        if defender["found"]:

            # attacker taking item on tile before fight
            if item_found["counter"] > 0 and board[night][2] is None:
                board = self.acquire_item(board,new_location,item_found,night)

            # check if there is a defender on location to make a fight
            res = self.fight(board[night], board[defender["key"]], new_location)
            board[night] = res["attacker"]
            board[defender["key"]] = res["defender"]

        else:
            board[night][0]=new_location

            if (new_location[0] > 8 or new_location[0] < 0) or (new_location[1] > 8 or new_location[1] < 0) :
                """
                 Check if the night is drowned, to put his items on last night location 
                """

                if board[night][2] is not None:

                    # move the item to the last location a night was on
                    board[board[night][2]][0] = current_location
                    board[board[night][2]][1] = False

            if item_found["counter"] > 0 and board[night][2] is None:

                """
                 if found item increase the value of a night attacks or defence according to the value of item found
                """
                board = self.acquire_item(board, new_location, item_found, night)

            else:
                # pass
                # move item held by night when a night move
                if (board[night][2] is not None) and (0 <= new_location[0] <= 8 and 0 <= new_location[1] <= 8):
                    board[board[night][2]][0] = new_location


                # print(board)







        return board



    def check_equiped_location(self):
        pass





