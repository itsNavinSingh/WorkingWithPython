# Love Calculator
Your_Name=input('Enter Your Name: ').lower()
Crush_Name=input("Enter Your Crush Name: ").lower()
Whole_Name=Your_Name+Crush_Name
total_count=Whole_Name.count('t')
total_count += Whole_Name.count('r')
total_count += Whole_Name.count('u')
total_count += Whole_Name.count('e')
total_count *= 10
total_count += Whole_Name.count('l')
total_count += Whole_Name.count('o')
total_count += Whole_Name.count('v')
total_count += Whole_Name.count('e')
print(f'Your Love Score is {total_count}, end="" ')
if total_count > 90 or total_count < 10:
    print(' You go together like coke and mentos.')
elif total_count >= 40 or total_count <= 50:
    print(' You are alright together.')
