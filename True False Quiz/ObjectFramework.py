from data import question_data
class Framework:
    def __init__(self, qdata):
        self.data = qdata
        self.Count = 0

    
    def QuestionAnswer(self, QuestionNo, UserInput):
        if self.data[QuestionNo-1]['answer'] == UserInput:
            self.Count += 1
