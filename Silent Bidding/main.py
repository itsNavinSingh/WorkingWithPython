import os
# Silent Bid 
Name_List = []
Bid_List = []
Bidder = True
while Bidder:
    Name = input('Enter Your Name:\n')
    Amount = int(input('Enter your Bidding Amount: $'))
    Name_List.append(Name)
    Bid_List.append(Amount)
    more = input('Is anyone else also want to Bid? Y for Yes, N for No\n').lower()
    if more == 'n':
        Bidder = False
    os.system('cls')
Max_Amount = max(Bid_List)
Position = Bid_List.index(Max_Amount)
Winner_Name = Name_List[Position]
print(f'{Winner_Name} win the Bidding with a bidding amount of ${Max_Amount}.')

# Asign grades of the students by creating new dictionary
Student_Scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
Student_Grades = {}
for name in Student_Scores:
    if Student_Scores[name] > 90:
        Student_Grades[name] = 'Outstanding'
    elif Student_Scores[name] > 80:
        Student_Grades[name] = 'Exceeds Expectations'
    elif Student_Scores[name] > 70:
        Student_Grades[name] = 'Acceptable'
    else:
        Student_Grades[name] = 'Fail'
print(Student_Grades)

# Silent Bid 2.0
def Bid_Winner(Dict):
    Winner = ['Winner', 'Bidding Amount']
    bid = 0
    for name in Dict:
        if Dict[name] > bid:
            bid = Dict[name]
            Winner[0] = name
            Winner[1] = bid
    return Winner
Info_Dict = {}
Another_Bidder = True
while Another_Bidder:
    Bider = input('Enter Your Name:\n')
    Bid = int(input('Enter Your Bidding Amount:\n$'))
    Info_Dict[Bider] = Bid
    Another = input('Is there any more bidder there? Yes or No\n').lower()
    if Another == 'no':
        Another_Bidder = False
    os.system('cls')
result = Bid_Winner(Info_Dict)
print(f'{result[0]} win the bid with a bidding amount of ${result[1]}.')