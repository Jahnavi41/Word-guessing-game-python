# This is a word guessing game implemented in python
#import random
import random

#Set number of guesses
c=6

lst=['apple','orange','litchi','mango']

to_guess=random.choice(lst)

guessed=''
print("The word to be guessed has following number of characters:")
while c>0:
    tried=0
    for i in to_guess:
        if i in guessed:
            print(i,end=" ")
        else:
            print("_",end=" ")
            tried+=1
    print()
    if tried==0:
        print()
        print("Congratulations!,You have won!!")
        break

    print()
    print("Start guessing")
    g=input("Enter alphabet:")
    print()
    if g in guessed:
        print("Guesssed already!")
        print()
        c-=1
        if c==0:
            print("Better luck next time!")
            
    guessed+=g
    if g not in to_guess:
        c-=1
        print("Wrong guess!")
        if c==0:
            print("Better luck next time!")