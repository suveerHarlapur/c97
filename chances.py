print("...Number Guessing Game...")
print("guess a number (beetween 1 and 9) :")
import random
number=random.randint(2,8)
guess=int(input("Enter A Number :"))
chances=5

while chances>0:
    if(guess==number):
        print("you won !!!")
        break
    else:
        chances-=1
        if(chances>0):
            print('the guessed number is incorrect it is not close to ',guess)
            print("remaining chances ",chances)
            guess=int(input("Enter A Number :"))
        elif(chances==0):
            print("game over the correct answer is",number)
            break
