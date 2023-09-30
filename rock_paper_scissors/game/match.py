class Match:
    '''Match keep track of who is winning in each round
    
    Args: 
        self._win: keep track if the player or the machine is winning.
    '''
    def __init__(self):
        """Constructs a new Match.
        
        Args: 
            self: an instance of Match
            
        """
        self._win = False
    def who_wins(self, player, machine):
        if player == "rock":
            if machine == "paper":
                return False
            elif machine == "scissors":
                return True
            elif machine == "rock":
                print("It is a tie")
        elif player == "paper":
            if machine == "scissors":
                return False
            elif machine == "rock":
                return True
            elif machine == "paper":
                print("It is a tie")
        elif player == "scissors":
            if machine == "rock":
                return False
            elif machine == "paper":
                return True
            elif machine == "scissors":
                print("It is a tie")
        
