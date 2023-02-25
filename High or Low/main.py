from Data import List_Of_Datas
import random
import os
List_Of_Data = List_Of_Datas
Correct = True
First_Data = random.choice(List_Of_Data)
while Correct and len(List_Of_Data) != 0:
    List_Of_Data.remove(First_Data)
    Second_Data = random.choice(List_Of_Data)
    print('Guess the Twitter Follower of 2nd personality with respect to 1st')
    for i in First_Data:
        if i != 'Follower_Count':
            print(f'{i}: {First_Data[i]}')
    print()
    print()
    print('VS')
    print()
    print()
    for j in Second_Data:
        if j != 'Follower_Count':
            print(f'{j}: {Second_Data[j]}')
    guess = input("Type Higher or Lower: ").lower()
    if guess == 'higher':
        Check = Second_Data['Follower_Count'] > First_Data['Follower_Count']
    else:
        Check = Second_Data['Follower_Count'] < First_Data['Follower_Count']
    if Check:
        os.system('cls')
        print('Correct!')
        First_Data = Second_Data
    else:
        Correct = False
        print('Wrong Answer!')
        print(f"{First_Data['Name']} has {First_Data['Follower_Count']}M but {Second_Data['Name']} has {Second_Data['Follower_Count']}M Follower on Twitter")
        break
if len(List_Of_Data) == 0:
    print('You are a genious. You have answerd all question correctly')

