from random import randint

t = ['Rock', 'Paper', 'Scissors']

computer = t[randint(0,2)]

player = False

while player == False:
    player = input('Rock, Paper, Scissors? ')
    if player == computer:
        print('Draw!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose!', computer, 'beats', player)
        else:
            print('You Win!', player, 'beats', computer)
    elif player == 'Paper':
        if computer == 'Scissors':
            print('You Lose!', computer, 'beats', player)
        else:
            print('You Win!', player, 'beats', computer)
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You Lose!', computer, 'beats', player)
        else:
            print('You Win!', player, 'beats', computer)
    else:
        print('Invalid answer. Please check your spelling!')
    
    player = False
    computer = t[randint(0,2)]