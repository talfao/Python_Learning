import random

def play():
    user = input("Choose your option: \n 'r' for rock \n 'p' for paper \n 's' for scissors \n Your option: ")
    computer = random.choice(['r','p','s'])
	
	print("computer chose: ", computer)
    if computer == user:
        return "Tie"

    if player_win(user, computer):
        return "You won!"

    
    return "You lost"


def player_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play())
