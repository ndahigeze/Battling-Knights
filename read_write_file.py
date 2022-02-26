import json


class ReadWriteFile:
    """
       Reading the Game play moves file
    """
    def read():
        f = open("moves.txt", "r")
        data=[]
        for x in f:
            if x !="GAME-START\n" and x !="GAME-END":
                data.append(x.replace("\n","").split(":"))
        return  data

    def write(board):
        json_string = json.dumps(board)
        with open('final_state.json', 'w') as outfile:
            outfile.write(json_string)






