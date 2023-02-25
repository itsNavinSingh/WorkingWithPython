# BMI calculator 2.0
height=float(input('Enter your height in m: '))
weight=int(input('Enter you weight in kg: '))
bmi=round(weight/(height**2),0)
if bmi>=35:
    review='Cliniclly obese'
elif bmi>=30:
    review='Obese'
elif bmi>=25:
    review='Overweight'
elif bmi>=18.5:
    review='Normal Weight'
else:
    review='Under Weight'
print(f'Your BMI is {bmi}, you are {review}')