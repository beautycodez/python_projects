class Player:
    '''Player represent the user in the game.
    
    Args: 
        self._election: store the input of the player.
    '''
    def __init__(self):
        """Constructs a new Player.
        
        Args: 
            self: an instance of Player
            
        """
        self._election = ""

    def get_election(self):
        return self._election

    def set_election(self, input):
        self._election = input


    
            
            
