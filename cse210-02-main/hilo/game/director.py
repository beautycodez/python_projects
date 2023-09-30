from game.card import Card
import random
class Director:
    def __init__(self):
        
        self.is_playing = True
        self.score = 0
        self.totalscore = 0
        self.card = random.randint(1,13)
        self.guess = ""
        
        

    def start_game (self):
        first_score = 300
        self.totalscore += first_score
        while self.is_playing:
            self.card = random.randint(1,13)
            print (f"The card is {self.card} ")
            self.get_inputs ()
            self.do_updates ()
            print ()
        print ("Game Over")
        


    def get_inputs(self):
        """Ask the user is they want to keep playing

        Arg: 
            Self (Director): An instance of Director
        """

        play_turn = input ("Higher or lower? [h/l]")
        # looking for the second card
        card = Card()
        second_card = card.see_card()
        print (f"The next card was: {second_card}")
        if play_turn == "h":
            if second_card >= self.card:
                self.score = 100
                self.totalscore += self.score 
                print (f"you guessed it, your score is {self.totalscore}")
            else:
                self.totalscore = self.totalscore - 75
                print (f"you didn't guess it, your score is {self.totalscore}")

        elif play_turn == "l":
            if second_card <= self.card:
                self.score = 100
                self.totalscore += self.score 
                print (f"you guessed it, your score is {self.totalscore}")
            else:
                self.totalscore = self.totalscore - 75
                print (f"you didn't guess it, your score is {self.totalscore}")

    def do_updates (self):
        if not self.is_playing:
            return
        # card = Card ()
        # self.card= card.see_card()  
        play_turn = input ("Play again? [y/n]")
        self.is_playing = (play_turn == "y")
        if self.totalscore <= 0:
            self.is_playing = False
    



    # def print_output (self):
    #     print (f"The car is: {self.card}")

    # def get_guess (self):
    #     self.guess = input ("Higher or lower? [h/l]")

        # play_turn = input ("Play again? [y/n]")
        # self.is_playing = (play_turn == "y")
    
        
        

        
        
