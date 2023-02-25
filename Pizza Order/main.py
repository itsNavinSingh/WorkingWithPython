# pizza order
print('Welcome to python pizza deliveries!')
size=input('What size pizza do you want? S, M or L: ')
add_paperoni=input('Do you want paperoni? Y or N: ')
extra_cheese=input('Do you want extra cheese? Y or N: ')
if size == 'S':
    pizza_prize=15
    if add_paperoni=='Y':
        pizza_prize +=2
elif size == 'M':
    pizza_prize=20
    if add_paperoni=="Y":
        pizza_prize += 3
else:
    pizza_prize=25
    if add_paperoni=='Y':
        pizza_prize += 3
if extra_cheese=="Y":
    pizza_prize += 1
print(f'Your final Bill is ${pizza_prize}')

