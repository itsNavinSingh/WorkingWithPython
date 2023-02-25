import os
import random

# Number Guessing game
Play_Again = True
while Play_Again:
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of number between 1 and 100.")
    Level = input('Choose a difficulty level. Type "easy" or "hard": ').lower()
    if Level == 'easy':
        Life_Left = 10
    else:
        Life_Left = 5
    Computer_Guess = random.randint(1,100)
    while Life_Left != 0:
        print(f'You have {Life_Left} attempts remaining to guess the number.')
        User_Guess = int(input('Make a guess: '))
        if User_Guess == Computer_Guess:
            print(f'You got it! The answer was {Computer_Guess}')
            break
        elif User_Guess > Computer_Guess:
            Life_Left -= 1
            print('Too high')
            print('Guess Again.')
        else:
            Life_Left -= 1
            print('Too low')
            print('Guess Again.')
    if Life_Left == 0:
        print('You have ran out of guesses, you lose')
        print(f'The answer was {Computer_Guess}.')
    Ask_Again = input('Do you want to play again? "yes" or "no": ').lower()
    if Ask_Again == 'yes':
        os.system('cls')
    else:
        Play_Again = False
        print('Thank You!')