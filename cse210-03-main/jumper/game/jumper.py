class Jumper:
    def __init__(self):
        self._letter = ""

    def move_letter(self, letter):
        ''' Get the letter from the user and save it.
        Arguments:
            self (jumper): An instance of get_letter.
            letter: The letter that the user wrote.
        Return:
            The letter'''
        
        self._letter = letter

    def get_letter (self):
        ''' Get the letter from the user and save it.
        Arguments:
            self (jumper): An instance of get_letter.
            
        Return:
            The letter'''

        letter = self._letter
        return letter

    def print_jumper (self):
        jumper = [
            ["  ____"],
            [" /____\\"],
            [" \\    /"],
            ["  \\  /"],
            ["    O"],
            ["   /|\\"],
            ["   / \\"],
            [""],
            ["^^^^^^^"]
        ]
        for i in range (len(jumper)):
            jumper_string = jumper[i]
            print (jumper_string)
            
            
