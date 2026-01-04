import random

#gets random num
def randomNum():
    realNum = random.randint(1,100)
    return realNum


#gets user guess, returns as int
def guessNum():
    guessNum = input('Please Enter a Guess Between 1-100: ')
    return int(guessNum)

#compares guess to real num
def compares(guessNum, realNum):
    guess = guessNum
    real = realNum
    #logic behind comparison
    if guess == real:
        print(f'Congrats! {real}')
    elif guess > real:
        print(f'Too High! {real}')
    else:
        print(f'Too Low! {real}')


#Main Loop Logic
playing = True

while playing:
    realNum = randomNum()
    guess = guessNum()
    compares(guess, realNum)


    #play again logic
    playAgain = True
    while playAgain:
        again = input('Do you want to play again? y/N: ')
        if again.upper() == 'Y':
            playing = True
            playAgain = False
        elif again.upper() == 'N':
            playing = False
            playAgain = False
        else:
            print('Invalid Choice!')
