import random
import os
def card():
    option = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    Selected_Cards = random.choice(option)
    return Selected_Cards

Again = 'yes'
while Again == 'yes':
    os.system('cls')
    Computer_Cards = []
    User_Cards = []
    for i in range(2):
        Computer_Cards.append(card())
        User_Cards.append(card())
    print(f'Your Cards are {User_Cards}')
    print(f'One Cards of the computer is {random.choice(Computer_Cards)}')
    Another_Card = input('Do you want another card: ').lower()
    while Another_Card == 'yes' and sum(User_Cards) < 21:
        User_Cards.append(card())
        print(f'Your Cards are {User_Cards}')
        if sum(User_Cards) <21:
            Another_Card = input('Do you want another card: ').lower()
    print()
    print('Result:- ')

    if sum(User_Cards) <= 21:
        while sum(Computer_Cards) < 16:
            Computer_Cards.append(card())
        if sum(User_Cards) > sum(Computer_Cards):
            print(f'Your Cards are {User_Cards} and Computer has {Computer_Cards}')
            print('You Win!!!')
        elif sum(User_Cards) < sum(Computer_Cards):
            print(f'Your Cards are {User_Cards} and Computer has {Computer_Cards}')
            print('You Loose!!!')
        else:
            print(f'Your Cards are {User_Cards} and Computer has {Computer_Cards}')
            print('Game Draw!!!')
    else:
        print(f'Your Cards are {User_Cards} and Computer has {Computer_Cards}')
        print(f'Bust!! You Lose!')
    Again = input('Do you want to play again: ').lower()