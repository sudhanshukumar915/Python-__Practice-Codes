#Heading
import random
#global variables
easy_level=10
hard_level=5
number_of_turn=0
guess=0

print("Welcome to Guessing number Game ")
def game():
        #computer choice means computer choose a random number between 1 and 100
        computer_number=random.choice(range(1,101))
        print(f'{"computer_number : "} {computer_number}')

        #guess number function
        def guess_number_fun(user_input,computer_number,number_of_turn):

            if user_input>computer_number:
                    print("GUESS TO HIGH ")
                    return number_of_turn -1
            elif user_input<computer_number:
                    print("GUESS TO LOW " )
                    return number_of_turn -1
            else :
                if user_input == computer_number:
                    print("YOU WIN ")

        #easy mode function
        def easy_mode_function(choose_mode):
           if choose_mode=="easy":
               return easy_level

        #hard mode function
        def hard_mode_function(choose_mode):
            if choose_mode=="hard":
                return hard_level



        choice_mode={"easy":'mode_easy()',
                     "hard":'mode_hard()'
                     }
        #user choose the mode
        choose_mode=input("Easy Mode or Hard Mode ?" ).lower()
        if choose_mode=="easy":
            easy_mode_function(print("you have only 10 attempts"))
        elif choose_mode=="hard":
            hard_mode_function(print("you have only 5 attempts"))
        else:
                print("invalid input")
                breakpoint()

        #user guess the number
        while guess!=computer_number:
            user_input=int(input("Guess the number : " ))
            print(guess_number_fun(user_input,computer_number,number_of_turn))
            if number_of_turn==0:
                print("YOUR all attempts lost")


game()






