## This is small guessing number game. Try to guess random number in interval. 
# program will guide you if your gues is too much high or low

from random import seed
from random import randint
print("Hi There!Lets play guessing game!")
print("Try to guess number from 1-10")
print("You have 10 guesses")
print("Type a number from 1 - 10:")
guess_list = []
seed()
ranNum = randint(1,10)
while len(guess_list) < 10:
    a = int(input())
    guess_list.append(a)

    if a == ranNum:
        print("Nice you are RIGHT! You WIN")
        break
    else:
        if a > ranNum:
            print("You are close but too HIGH!")
        else: 
            print("You are close but too LOW!")    
else:
    print("You reached maximum guesses")
