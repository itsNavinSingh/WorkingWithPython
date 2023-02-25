from coffeedata import resource, MENU, Money_Type
import os
def Resource_Avaliable(a):
    out = 'Avaliable:\n'
    for i in a:
        out += f'{i}: {a[i]} ml\n'
    return out


def Coffee_Cost(a):
    list_item = MENU
    Coffee_Menu = MENU[a]['cost']
    return Coffee_Menu

money = 0
exit = False
while not exit:
    Ask_Order_Report = input('order, report, refill:  ').lower()
    if Ask_Order_Report == 'report':
        print(Resource_Avaliable(resource))
        print(f'Money Stored: ${money}')
    elif Ask_Order_Report == 'order':
        Order = input('What would you like to have? "espresso", "latte", "cappuccino": ')
        print(f'It will cost you ${Coffee_Cost(Order)}.')
        Pay = 0
        for i in Money_Type:
            Pay += int(input(f'{i}: '))*Money_Type[i]
        if MENU[Order]['ingredients']['water'] <= resource['water'] and MENU[Order]['ingredients']['milk'] <= resource['milk'] and MENU[Order]['ingredients']['coffee'] <= resource['coffee']:
            if Coffee_Cost(Order) <= Pay:
                resource['water'] -= MENU[Order]['ingredients']['water']
                resource['milk'] -= MENU[Order]['ingredients']['milk']
                resource['coffee'] -= MENU[Order]['ingredients']['coffee']
                money += Coffee_Cost(Order)
                print(f'Here is your ${Pay - Coffee_Cost(Order)}')
                print(f'Here is your {Order}')
                print('Thank You!')
            else:
                print('Low balance. Your money has been refunded.')
        else:
            print('Insufficent Resources!')
    elif Ask_Order_Report == 'refill':
        for i in resource:
            resource[i] = resource[i] + int(input(f'{i}: '))
        print('Refilled Successfully!')

    else:
        print('Invalid input')
    Ask_Exit = input('Do you want to continue or exit: ').lower()
    if Ask_Exit == 'exit':
        exit = True
        print('Thank You')
    else:
        os.system('cls')