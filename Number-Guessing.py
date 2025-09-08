import random

print('Welcome To Number Guesing Game!')
print('Guss The Number Between 1 To 50 !')
print('To exit in mid of the Game press 0')

computer_choise=random.randint(1,50)
attempts=5

while attempts>0:

    print(f"Attempts left:{attempts}")

    try:
        guess=int(input("Enter your guess:"))

        if guess==0:
            print('Over The Game!')
            break

        if guess==computer_choise:
            print('Congratulations! You guessed Right number:')
            break

        elif guess<computer_choise:
            print('Too low! Try a higher number')

        elif guess>computer_choise:
            print('Too high! Try a lower number')

        else:
            if guess=='Exit':
                break

        attempts-=1

    except ValueError:
             print('Invalid input.Please enter a number.')

if attempts==0:
    print(f"Game Over! The number was {computer_choise}")


