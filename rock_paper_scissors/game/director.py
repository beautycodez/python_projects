from game.terminal_service import TerminalService
from game.player import Player
from game.machine import Machine
from game.match import Match
from game.scores import Scores




class Director:
    '''The director sets the turns of the game.
    Args:
        self._is_playing: determined when the game is on going
        self._terminal_service : an instance of TerminalService
        self._election : an instance of Player
        self._machine_election : an instance of Machine
        self._scores: an instance of Scores
        self._rock_paper_scissors: store the variable of the player
        self._machine_rock_paper_scissors: store the random variable of the machine
        self._player_win: store the status of each round
    '''

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self: an instance of Director
            
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._election = Player()
        self._machine_election = Machine()
        self._scores = Scores()
        self._rock_paper_scissors = ""
        self._machine_rock_paper_scissors =""
        self._player_win = False
    
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """get the inputs from the user and loop if the input is not acceptable for the game.

        Args:
            self (Director): An instance of Director.
        """
        repeat = True
        # or choose !="paper" or choose != "scissors":
        while repeat == True:
            choose = self._terminal_service.read_text("What is your choice? (rock/paper/scissors): ")
            self._election.set_election(choose)
            if choose == "rock":
                repeat= False
            elif choose == "paper":
                repeat = False
            elif choose == "scissors":
                repeat = False
            else:
                repeat = True

    def _do_updates(self):
        """get the inputs and calculate the points if you win or lose.

        Args:
            self (Director): An instance of Director.
        """
        self._rock_paper_scissors = self._election.get_election()
        self._machine_rock_paper_scissors = self._machine_election.get_random_election()
        
        match = Match()
        self._player_win = match.who_wins(self._rock_paper_scissors,self._machine_rock_paper_scissors)
        if self._player_win == True:
            status = "win"
            self._scores.calculate_score(status)
        elif self._player_win == False:
            status = "lose"
            self._scores.calculate_score(status)



       
    def _do_outputs(self):
        """ print the information to know the status of the game.

        Args:
            self (Director): An instance of Director.
        """
        print()
        print (f"You chose {self._rock_paper_scissors}")
        print (f"The machine chose {self._machine_rock_paper_scissors}")
        if self._player_win == True:
            print()
            print ("<<<<<<<you win>>>>>>>")
            print()
        elif self._player_win == False:
            print()
            print ("<<<<<<<you lose>>>>>>>")
            print()

        scores = self._scores.get_score()
        print ("----------------")
        print (f"Your score is {scores}")
        print ("----------------")
        print()
      
        if scores == 0:
            print ("GAME OVER")
            self._is_playing = False