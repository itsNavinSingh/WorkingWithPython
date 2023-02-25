import random
# banker Roulette
names=input("Give me everybody's names, seperated by a comma.\n") 
Bankers=names.split(', ')
# we can pick a bancker by using "random.choice(Bankers)" function
Picked_Banker=Bankers[random.randint(0,len(Bankers)-1)]
print(f'{Picked_Banker} is going to buy the meal today!')
