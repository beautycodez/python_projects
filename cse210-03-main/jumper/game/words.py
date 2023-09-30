import random
class Words:
    """The words that the jumper will guess. 
    
    The responsibility of Words is create and chose words from a list with the purpose of guessing. 
    
    Attributes:
        _words (int): A list of words.
        
    """
    def __init__(self):
        self._words = []
        self._word = ""
        self._spaces = []



    def choose_word (self):
        '''Create a list of words and return a word randomly
        Args: 
            self (Words): An instance of choose_word.
'''
        
        self._words = ["big", "beautiful", "small", "smart", "tall", "huge", "fast"]
        self._word = random.choice(self._words)
        

    def get_word (self):
        return self._word

    def decompose_word (self):
        word_to_list = list(self._word)
        
        return word_to_list

    def check_letter (self, letter):
        '''replace the letter in the self._spaces list'''
        word_to_list = self.decompose_word ()
        index = word_to_list.index(letter)
        self._spaces [index] = letter
        return (self._spaces)
        

        

    
    def print_spaces (self):
        spaces_len = len(self._spaces)
        word_list = self.decompose_word()
        if spaces_len == 0:
            
            
            for i in range (len(word_list)):
                word_list [i] = "_ "
                self._spaces.append(word_list[i])
            print (self._spaces)
        else:
                
            print (self._spaces)




    def game_over (self):
        len_spaces = len(self._spaces)
        count = -1
        for i in range (len_spaces):
            if self._spaces[i] == self._word[i]:
                count += 1
        if count == len_spaces:
            return False
        else:
            return True

            