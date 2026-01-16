import time
bhoot=['''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣶⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣾⣿⣿⠏⡀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⠟⣡⣴⣾⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡿⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣇⣿⣿⣿⡟⠁⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣤⣤⡀⢀⣿⣿⣿⠟⠛⠻⣿⣿⡇⢀⣀⢠⡿⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠿⣿⣿⣿⣿⣿⣟⡁⠀⠀⢀⣿⣿⡇⢸⣿⣿⣷⡾⠛
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⠀⡘⠉⢻⣿⣿⣿⣿⣷⣄⣾⣿⡿⠀⣾⣿⡿⠿⠿⠖
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⡄⠀⠀⠘⠛⣿⣿⣿⣿⣟⣥⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣿⣿⣿⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠛⠻⠿⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''']
word_list=["goodnight","cosmos","wolf","nightwalker","darkworld","manupulater"]
#choose a  random word for Word_list
import random
random_word=random.choice(word_list)
#print("THE RANDOM WORD IS : "+random_word)
#place hold
placeholder=""
word_length=len(random_word)
for position in range(word_length):
    placeholder +="_ "
print(placeholder)     #THIS IS OUTSIDE THE LOOP
##user choose/guess a word the word
game_over= False
correct_latter=[]
while not game_over:
    guess=input("Enter the choosen word : ").lower()
    print(guess)

    fix_letter=""
    for letter in random_word:
        if letter == guess:
           fix_letter+=letter
           correct_latter.append(guess)
        elif letter in random_word:
            fix_letter+=letter
        else:
            fix_letter+="_"

    print(fix_letter)

    if "_" not in fix_letter:
        game_over = True
        print("YOU WIN")

    if guess  not in random_word:
       game_over=True
    print("YOU LOSE"+bhoot)





time.sleep(5)    #THIS FUNCTION IS PERFORM ANIMATION OF TIME DELAY
print("ALL THE WORK IS DONE BY SS")


