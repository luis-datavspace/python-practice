import random
def main ():
    
    
    '''
    1 es para '✊' (Roca)
    2 es para '✋' (Papel)
    3 es para '✌️' (Tijeras)
    4 es para '🦎' (Lizard)
    5 es para '🖖' (Spock)
    '''
    
    
    print('''
        ================================
        Rock Paper Scissors Lizard Spock
        ================================
            ''')
    
    print('''
        1) ✊
        2) ✋
        3) ✌️
        4) 🦎
        5) 🖖
                ''')
    
    
    
    options = [1,2,3,4,5]
    
    
    player = int(input("Pick a number: "))
    
    if player not in options:
        return 'Incorrect option'
    
    computer = random.randint(1,5)
    
    print(f"Your choise was {'✊' if player == 1 else '✋'if  player == 2 else '✌️' if player == 3 else '🦎' if player == 4 else '🖖' }")
    print(f"The computer choise was {'✊' if computer == 1 else '✋'if  computer == 2 else '✌️' if computer == 3 else '🦎' if computer == 4 else '🖖' }")
    print(ganador(player, computer))
    
    
    
def ganador (player,computer):
    
    if player == computer:
        return 'It is a draw'
    elif (
            (player == 1 and (computer == 3 or computer == 4)) or
            (player == 2 and (computer == 1 or computer == 5)) or
            (player == 3 and (computer == 2 or computer == 4)) or
            (player == 4 and (computer == 2 or computer == 5)) or
            (player == 5 and (computer == 3 or computer == 1)) 
        ):
        return 'You Won'
    else:
        return 'You Lose'

main()
