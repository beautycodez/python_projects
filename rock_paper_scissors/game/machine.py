import random
class Machine:
    '''Machine represent the opponent in the game
    
    Args: 
        self._machine_election: store the random election of the machine
    '''
    def __init__(self):
        """Constructs a new Machine.
        
        Args: 
            self: an instance of Machine
            
        """
        self._machine_election = ""

    def random_election(self):
        rock_paper_scissors_list = ["rock","paper","scissors"]
        rock_paper_scissors = random.choice(rock_paper_scissors_list)
        self._machine_election = rock_paper_scissors
    def get_random_election(self):
        self.random_election()
        return self._machine_election
