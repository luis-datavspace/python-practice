import random
def main ():
    
    
    '''
    1 es para '✊' (Roca)
    2 es para '✋' (Papel)
    3 es para '✌️' (Tijeras)
    4 es para '🦎' (Lizard)
    5 es para '🖖' (Spock)
    '''
    
    
    print('WELCOME TO THE GAME OF ROCK, PAPER AND SCISSORS')
    
    options = [1,5]
    
    player = int(input("Pick a number: 1 '✊' (Rock), 2 is for '✋' (Paper), 3 is for '✌️' (Scissors), 4 is for '🦎' and 5 is for '🖖'"))
    
    if player not in options:
        return 'Incorrect option'
    
    computer = random.randint(1,5)
    
    print(f"Your choise was {'✊' if player == 1 else '✋'if  player == 2 else '✌️' if player == 3 else '🦎' if player == 4 else }")
    print(f"The computer choise was {'✊' if computer == 1 else '✋'if  computer == 2 else '✌️'}")
    print(ganador(player, computer))
    
    
    
def ganador (player,computer):
    
    if player == computer:
        return 'It is a draw'
    elif (
            (player == 1 and computer == 3) or
            (player == 2 and computer == 1) or
            (player == 3 and computer == 2) or
            (player == 4 and computer ==) 
        ):
        return 'You Won'
    else:
        return 'You Lose'

main()