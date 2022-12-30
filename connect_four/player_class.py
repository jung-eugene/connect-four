from board_class import Board

class Player:
    """ a Player class to represent a player of the Connect Four 
    """
    def __init__(self, checker):
        """ constructor that initializes the attribute  
            in every Player object (checker)
        """
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object 
        """
        return 'Player ' + str(self.checker)
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker 
            of the Player object’s opponent
        """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'
        
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns 
            the column where the player wants to make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
    
