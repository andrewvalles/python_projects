import random

#gets dice roll
def get_dice():
    dice_roll = random.randint(1,6)
    return dice_roll

#asks user if they want to play
def playGame():
    play = input('Do you want to test your luck? Roll Snake Eyes or Doubles to win: r/R ')
    return play.upper()

#compares dice rolls
def evaluate(dice1, dice2):
    if dice1 == 1 and dice2 ==1:
        print(f'Snake Eyes! You win! {dice1}, {dice2}')
    elif dice1 == dice2:
        print(f'Doubles, close enough. You win! {dice1}, {dice2}')
    else:
        print(f'You lose! Try again {dice1}, {dice2}')

#asks to play again
def playAgain(playing):
    playAgain = True
    while playAgain:
        again = input('Do you want to play again[y/N]? ')
        if again.upper() == 'Y':
            playing = True
            playAgain = False
        elif  again.upper() == 'N':
            playing = False
            playAgain = False
        else:
            print('Invalid Input. Try Again!')
    return playing


#calls function to start game
playGame()

#main logic loop
playing = True
while playing:
    dice1 = get_dice()
    dice2 = get_dice()
    evaluate(dice1, dice2)
    playing = playAgain(playing)

