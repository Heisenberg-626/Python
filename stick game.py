'''
Author: Sourav V S
Date: 03-12-2024
This program is to play a stick game.
'''
def stick_game():
    player_1 = input("Who is player 1 ? ")
    player_2 = input("Who is player 2 ? ")
    current_player = 0
    total_sticks = 16
    while total_sticks > 0:
        current_player = player_1
        p1_sticks = int(input(f"{player_1}, pick 1, 2 or 3 sticks: "))
        rem_sticks = total_sticks - p1_sticks
        print("Remaining sticks: ", rem_sticks)
        total_sticks = rem_sticks
        current_player = player_2
        p2_sticks = int(input(f"{player_2}, pick 1, 2 or 3 sticks: "))
        rem_sticks = total_sticks - p2_sticks
        print("Remaining sticks: ", rem_sticks)
        total_sticks = rem_sticks
        if rem_sticks <= 0:
            print(f"{current_player}, you lose!")
            break
stick_game()