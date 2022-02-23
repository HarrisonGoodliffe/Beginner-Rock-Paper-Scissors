from random import randint

X = ['Rock', 'Paper', 'Scissors']
Score = int(0)


Computer = X[randint(0,2)]

Player = False

while Player == False:
    Player = input('Rock, Paper, Scissors? ')
    if Player == Computer:
        print('Draw!')
    elif Player == 'Rock':
        if Computer == 'Paper':
            print('You lose!', Computer, 'beats', Player)
            Score = 0
        else:
            print('You Win!', Player, 'beats', Computer)
            Score = Score + 1
    elif Player == 'Paper':
        if Computer == 'Scissors':
            print('You Lose!', Computer, 'beats', Player)
            Score = 0
        else:
            print('You Win!', Player, 'beats', Computer)
            Score = Score + 1
    elif Player == 'Scissors':
        if Computer == 'Rock':
            print('You Lose!', Computer, 'beats', Player)
            Score = 0
        else:
            print('You Win!', Player, 'beats', Computer)
            Score = Score + 1
    else:
        print('Invalid answer. Please check your spelling!')
    
    Player = False
    Computer = X[randint(0,2)]
    print('Score:', Score)