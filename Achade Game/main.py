# archade game
print('Welcome to treasure Island.\nYour mission is to find the treasure.')
First_Step=input('Make a choice between left or right. ').lower()
if First_Step == 'left':
    Second_Step=input("Do you want to SWIM or WAIT for boat? ").lower()
    if Second_Step == 'wait':
        Third_Step=input('Which door you want to Open? Red, Blue or Yellow ').lower()
        if Third_Step == 'Yellow':
            print('You Won The gave.')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')
