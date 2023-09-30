# The program must have a comment with assignment and author names: 
# Angello Ruiz - all the programme.
# The program must have at least one if/then block.
# The program must have at least one while loop.
# The program must have more than one function.
# The program must have a function called main.
def main ():
    print ("1|2|3")
    print ("-+-+-")
    print ("4|5|6")
    print ("-+-+-")
    print ("7|8|9")
    first_numbers = [1,2,3]
    second_numbers =[4,5,6]
    third_numbers = [7,8,9]
    game = True
    while game == True:
        table_player1(first_numbers, second_numbers,third_numbers)
        game = check_winners(first_numbers, second_numbers,third_numbers)
        if game == True:
            table_player2(first_numbers, second_numbers,third_numbers)
            game = check_winners(first_numbers, second_numbers,third_numbers)
    print ("Thank you for playing")



# def check_movementx (first_numbers, second_numbers,third_numbers):
    
#     if first_numbers[0] == "o":
#         print ("change your game and choose another number")
#         return "bad"
#     elif first_numbers[0] != "o":
#         return "good"
             

def table_player1 (first_numbers, second_numbers,third_numbers):
    player1 = int(input("Player 1, enter a number between 1-9:"))
    replace_number_x (first_numbers, second_numbers,third_numbers,player1)
 
    
    




    

def table_player2 (first_numbers, second_numbers,third_numbers):
    player2 = int(input("Player 2, enter a number between 1-9:"))
    replace_number_o (first_numbers, second_numbers,third_numbers,player2)



def check_winners (first_numbers, second_numbers,third_numbers):
    # Rows
    if first_numbers[0] == first_numbers[1] and first_numbers[0]== first_numbers[2]:
        print ("You win the game")
        return False
    elif second_numbers[0] == second_numbers[1] and second_numbers[0] == second_numbers[2]:
        print ("You win the game")
        return False
    elif third_numbers[0] == third_numbers[1] and third_numbers[0] == third_numbers[2]:
        print ("You win the game")
        return False
    #columns
    elif first_numbers[0] == second_numbers[0] and first_numbers[0] == third_numbers[0]:
        print ("You win the game")
        return False
    elif first_numbers[1] == second_numbers[1] and first_numbers[1] == third_numbers[1]:
        print ("You win the game")
        return False
    elif first_numbers[2] == second_numbers[2] and first_numbers[2] == third_numbers[2]:
        print ("You win the game")
        return False
    #diagonals
    elif first_numbers[0] == second_numbers[1] and first_numbers[0] == third_numbers[2]:
        print ("You win the game")
        return False
    elif first_numbers[2] == second_numbers[1] and first_numbers[2] == third_numbers[0]:
        print ("You win the game")
        return False
    elif first_numbers[0] != 1 and first_numbers[1] != 2 and first_numbers[2] != 3 and second_numbers[0] != 4 and second_numbers[1] != 5 and second_numbers[2] != 6 and third_numbers[0] != 7 and third_numbers[1] != 8 and third_numbers[2] != 9:
        print ("It is a DRAW! Nice game.")
        return False
    
    else:
        return True


def replace_number_x (first_numbers, second_numbers,third_numbers,player1):
    if player1 >=1 and player1 <= 3:
        player1 = player1 - 1     
        first_numbers [player1] = "x" 
        print_table (first_numbers,second_numbers,third_numbers)
        

    elif player1 >=4 and player1 <= 6:
        player1 = player1 - 4
        second_numbers [player1] = "x"
        print_table (first_numbers,second_numbers,third_numbers)

    elif player1 >=7 and player1 <= 9:
        player1 = player1 - 7
        third_numbers [player1] = "x"
        print_table (first_numbers,second_numbers,third_numbers)






def replace_number_o (first_numbers, second_numbers,third_numbers,player2):
    if player2 >=1 and player2 <= 3:
        player2 = player2 - 1
        first_numbers [player2] = "o"
        print_table (first_numbers,second_numbers,third_numbers)

    elif player2 >=4 and player2 <= 6:
        player2 = player2 - 4
        second_numbers [player2] = "o"
        print_table (first_numbers,second_numbers,third_numbers)

    elif player2 >=7 and player2 <= 9:
        player2 = player2 - 7
        third_numbers [player2] = "o"
        print_table (first_numbers,second_numbers,third_numbers)




    
def print_table (first_numbers,second_numbers,third_numbers):
    print (f"{first_numbers[0]}|{first_numbers[1]}|{first_numbers[2]}")
    print ("-+-+-")
    print (f"{second_numbers[0]}|{second_numbers[1]}|{second_numbers[2]}")    
    print ("-+-+-")
    print (f"{third_numbers[0]}|{third_numbers[1]}|{third_numbers[2]}")






if __name__ == "__main__":
    main() 