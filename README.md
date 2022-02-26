# Battling Knights
## Note To run This program requires python  3.7

There is no specific library to install as long as python 3.7 is used but it is always good to create virtual environment for python project


This Game is build with several classes

### MainGameHandler class

-> This a class which start the game 
#### It Has:
 ->board dictionary which include the initial state of the board
  >  board = {
        "R": [[0, 0], "LIVE", None, 1, 1],
        "B": [[7, 0], "LIVE", None, 1, 1],
        "G": [[7, 7], "LIVE", None, 1, 1],
        "Y": [[0, 7], "LIVE", None, 0, 0],
        "A": [[2, 2], False],
        "M": [[5, 2], False],
        "H": [[5, 5], False],
        "D": [[2, 5], False],
    }

* `is_night` method to check if a key from board is a night
 
* `apply_instructions` methods to apply all move written in `moves.txt` file
 

### ReadWriteFile class
-> This class is used to read instructions from file and write the gamee results to json file

### Play class

This a class which handle all instructions from instruction file
 
#### It has:
* `items_priorities` dictionary to show the items priority
* `items` array to show the list of items keys
* `nights` array to show the list of night keys 
* `move` method which is a general method to handle each given instruction 

* `find_location` method which find the location where the night will move to

* `get_best_item` method which get item on tile if there are two it gets the best item

* `find_item_value` method which find the value of given item

* `check_another_night` method to check if there is another night already on the location

* `fight method which` method to handle find and return the loser and the winder 

* `acquire_item which` method to allow a night to acquire new item

Usage

#### Running the application 
 > python main.py

* Moves or instructions are in `moves.txt` file
* The result of the game is writen in `final_state.json` file


  



    


