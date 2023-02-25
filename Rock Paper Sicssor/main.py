import random
# Rock Paper and Scissor game
Value = ['Rock', 'Scissor', 'Paper']
Computer_Value = Value[random.randint(0,2)]
User_Value = Value[int(input('1. for Rock, 2. for Scissor, 3. for Paper\n'))-1]
print(f'You chose {User_Value}.')
print(f'Computer chose {Computer_Value}.')
if User_Value == Value[0]:
    if Computer_Value == Value[0]:
        print('Game draw!')
    elif Computer_Value == Value[1]:
        print('You Win!')
    else:
        print('You lose!')
elif User_Value == Value[1]:
    if Computer_Value == Value[1]:
        print('Game draw!')
    elif Computer_Value == Value[2]:
        print('You Win!')
    else:
        print('You lose!')
else:
    if Computer_Value == Value[2]:
        print('Game draw!')
    elif Computer_Value == Value[0]:
        print('You Win!')
    else:
        print('You lose!')