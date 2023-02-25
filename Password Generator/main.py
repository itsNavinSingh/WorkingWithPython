# Password Generator
import random
# Our character, number and special character stored in a list here
Letter = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
Lower_Case = Letter.split()
Upper_Case = (Letter.upper()).split()
Special_Character = ['!','@', '%', '&', '*']
Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# here we take input fom user about their password size and composition
Input_Lowercase = int(input('Please enter the number of lowercase letter you want: '))
Input_Uppercase = int(input('Please enter the number of uppercase letter you want: '))
Input_Specialcharacter = int(input('Please enter the number of special character you want: '))
Input_Number = int(input('Please enter the number of digits you want: '))
Total_Digit = Input_Lowercase + Input_Uppercase + Input_Specialcharacter + Input_Number
# We created the output list where we store the randomlly generated password elements
Output = []
# here i am storing the randomlly string in out output list 
for upper in range(0,Input_Uppercase):
    Output.append(random.choice(Upper_Case))
for lower in range(0,Input_Lowercase):
    Output.append(random.choice(Lower_Case))
for special in range(0,Input_Specialcharacter):
    Output.append(random.choice(Special_Character))
for num in range(0,Input_Number):
    Output.append(random.choice(Number))
# here i am randomlly displaying our password which stored in our output list and deleating the displayed string from our output list 
print('Generated Password is: ',end='')
PassWord = ''
for i in range(0,Total_Digit):
    a = random.choice(Output)
    PassWord += str(a)
    Output.remove(a)
print(PassWord)
