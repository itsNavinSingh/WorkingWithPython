# Tip Calculator
print('Welcome to the tip calculator.')
bill=float(input('What was the total bill?  $'))
split=int(input('How many people to split the bill? '))
tip=float(input('What percentage tip would you like to give? 10, 12, 15 or more?'))
total = bill + (bill*tip/100)
each=round(total/split,2)
print(f'Each person should pay: ${each}')
