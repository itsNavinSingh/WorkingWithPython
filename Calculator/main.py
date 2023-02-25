import os
# Calculator
def multi(a,b):
    return a*b
def sub(a,b):
    return a-b
def add(a,b):
    return a+b
def div(a,b):
    return a/b
Restart = True
while Restart:
    Continue = True
    first = float(input('Enter your 1st Number: '))
    while Continue:
        print('+\n-\n*\n/')
        Sign = input('Enter the operator: ')
        second = float(input('Enter your Second Number: '))
        match Sign:
            case '+':
                Program_Conter = add(first,second)
            case '-':
                Program_Conter = sub(first,second)
            case '*':
                Program_Conter = multi(first,second)
            case '/':
                Program_Conter = div(first,second)
        print(f'The output of {first}{Sign}{second} is {Program_Conter}')
        first = Program_Conter
        ask = input('Do you want to continue, restart or close\n').lower()
        match ask:
            case 'continue':
                os.system('cls')
            case 'restart':
                Continue = False
                os.system('cls')
            case 'close':
                Continue = False
                Restart = False