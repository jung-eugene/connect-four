import random  
from game import *

class AIPlayer(Player):
    """ a class to represent an AI player of the Connect Four """
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor that initializes the attribute  
            in every AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object """
        player = 'Player ' + str(self.checker)
        tb = str(self.tiebreak)
        la = str(self.lookahead)
        return player + ' (' + tb + ', ' + la + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
            board and returns the index of the column with the maximum score
        """
        col = []
        
        for i in range(len(scores)):
            if scores[i] == max(scores):
                col += [i]
        
        if self.tiebreak == 'LEFT':
            return col[0]
        elif self.tiebreak == 'RIGHT':
            return col[-1]
        else:
            return random.choice(col)
    
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores 
            for the columns in b
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, \
                               self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 100:
                    scores[col] = 0
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move """
        self.num_moves += 1
        
        return self.max_score_column(self.scores_for(b))
                
# play with an ai player!
# connect_four(Player('X'), AIPlayer('O', 'RANDOM', 3))          
        
        
        
        
        
        
        
        
        
        
        
        
        