from ObjectFramework import Framework
from data import question_data

QestionNo =0
Person1 = Framework(question_data)
while QestionNo != len(question_data):
    Rspo = input(f'{question_data[QestionNo]["text"]} (True/False):  ').title()
    Person1.QuestionAnswer(QestionNo, Rspo)
    QestionNo += 1


print(f"You have given total {Person1.Count} correct answer")
