# Stone Paper scissor Game (Concept)

# 1.Ask the users  how many round  are playing the game
# 2.User input=Enter your choice
# 3.if user input is space or not match the random value print("invalid syntax")
# 4.if users input == random.choice()
#  print(Tie)
# 5.if user choice stone  and random choice is paper
# print( loss )
# 6.if user choice paper  and random choice is stone
# print(win)
# 7.if user choice paper and random choice is scissor
# print(loss)
# 8.if user choice scissor and random choice is paper
# print(win)
# 9.if user choice stone  and random choice is scissor
# print(win)
# 10.if user choice scissor  and random choice is stone
# print(loss)
# AND after 5 round calculate total win of users and total loss of users and calculate
# the final result and declare match winner ...

# ----------------------------------------------------------------------------
import random
import sys

print("WELCOME TO STONE,PAPER OR SCISSOR GAME")

round_num = int(input("Enter how many round you play this game:-"))

user_win=0
computer_win=0
draw_=0

for user_input in range(0, round_num):
    # .lower() use for change the str into small letter and .strip() use to delete the space
    user_input = input("Enter your choice stone/paper/scissor:-").lower().strip()

    valid_choices = ["stone", "paper", "scissor"]
    if user_input not in valid_choices:
        sys.exit("Invalid syntax, please write valid syntax")

    computer_choice = random.choice(valid_choices)
    print(computer_choice)

    if user_input == computer_choice:
        print("Tie")
        draw_+=1

    if user_input == "paper" and computer_choice == "scissor":
        print("You lose!")
        computer_win+=1

    if user_input == "scissor" and computer_choice == "paper":
        print("You win!")
        user_win+=1

    if user_input == "stone" and computer_choice == "paper":
        print("You loss!")
        computer_win+=1

    if user_input == "paper" and computer_choice == "stone":
        print("You win!")
        user_win+=1

    if user_input == "stone" and computer_choice == "scissor":
        print("You win!")
        user_win+=1

    if user_input == "scissor" and computer_choice == "stone":
        print("You loss!")
        computer_win+=1

# Final result
print("Game over")
print(f"Total wins:{user_win}")
print(f"Total loss:{computer_win}")
print(f"Total draw:{draw_}")

if user_win>computer_win:
    print("YOU WON THE MATCH!")
elif computer_win>user_win:
    print("YOU LOSS THE MATCH!")
else:
    print("DRAW THE MATCH!")
