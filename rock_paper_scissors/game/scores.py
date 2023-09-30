class Scores:
    '''Scores calculate the scores of the game and add or take point depending on the 
    result of each round
    
    Args: 
        self._total_score: keep track of the points during the game
    '''

    
    def __init__(self):
        """Constructs a new Scores.
        
        Args: 
            self: an instance of Scores
            
        """
        self._total_score = 4 

    def calculate_score(self, status):
        if status == "win":
            self._total_score += 1
        elif status == "lose":
            self._total_score -= 1

    def get_score(self):
        return self._total_score