from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.words import Words


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._words = Words()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._jumper = Jumper()
    
        
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
        """get the word from a list
        get the letter by the user.

        Args:
            self (Director): An instance of Director.
        """
        #It just generate the word and save it.
        
        self._words.choose_word()
        self._words.print_spaces()
        self._jumper.print_jumper()
        
        new_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        self._jumper.move_letter(new_letter)
      
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # self._words.decompose_word()
        self._words.check_letter(self._jumper.get_letter())
        
        letter = self._jumper.get_letter()
        word_guess = self._words.check_letter(letter)
        
        # print (word_guess)
       
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        # self._words.print_spaces()
        # self._jumper.print_jumper()

        # word = self._words.get_word()
        
        
        
        
        self._is_playing = self._words.game_over()