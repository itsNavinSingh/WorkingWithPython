# rollercoster for mid life crisis person
print('Welcome to RollerCoster!')
height_new = int(input('Enter Your Height in cm: '))
if height_new >= 120:
    print('You can ride the Roller Coster')
    age_new=int(input('Enter your age: '))
    if age_new >= 45 and age_new <= 55:
        bill=0
    elif age_new >= 18:
        bill=12
    elif age_new >= 12:
        bill=7
    else:
        bill=5
    photo_new=input('Do you want extra Photo? Y or N: ')
    if photo_new == 'Y':
        bill += 3
    print(f'The total bill is ${bill}')
else:
    print('You Cannot ride the Roller Coster')