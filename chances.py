chances = 5
guessnumber = input('type a number between 1 and 9  ')
print('guessed number  ',guessnumber)
if(chances>=0):
    if(guessnumber=='2'):
        print('the guess is incorrect ,it is not so close to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)

    if(guessnumber=='3'):
        print('the guess is incorrect ,it is a little to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)
    if(guessnumber=='4'):
        print('the guess is incorrect ,it is little close to correct guess')
        print('chances remaining')
        chances=chances-1 
        print(chances)
    if(guessnumber=='5'):
        print('the guess is incorrect ,it is  close to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)
    if(guessnumber=='6'):
        print('the quess is correct you won the game')
        print('yoy still have ')
        print(chances)
    if(guessnumber=='7'):
        print('the guess is incorrect ,it is a little far to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)
    if(guessnumber=='8'):
        print('the guess is incorrect ,it is little far to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)
    if(guessnumber=='9'):
        print('the guess is incorrect ,it is not so close to correct guess')
        print('chances remaining')
        chances=chances-1
        print(chances)
elif(chances=='0'):
    print('chances over soo game is over')