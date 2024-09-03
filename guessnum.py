import random
num=random.randint(1,10)
guess=0
while(guess!=num):
    guess=int(input("Guess the number"))
    if(guess>num):
        print("The number you guessed is greatest than the actual number")
    elif(guess<num):
        print("The number you gussed is smaller than the actual number")
    else:
        print("You guessed the right number")