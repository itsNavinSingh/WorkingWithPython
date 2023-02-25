# Hangman 0.0
import random
Selected_Word = random.choice(input('Enter your sentences here\n').split())
Selected_Word_list = []
for i in Selected_Word:
    Selected_Word_list.append(i)
Guess_list = []
Guess_Word = ''
for i in range(len(Selected_Word)):
    Guess_list.append('_')
    Guess_Word += '_'
Life_Left = 2*len(Guess_list)
print(f'Remember You have {Life_Left} life')
while Selected_Word_list != Guess_list and Life_Left != 0:
    print(Guess_Word)
    Input_Sentence = input('Guess the letter\n')
    if len(Input_Sentence) == 1:
        counter = 0
        for i in range(len(Selected_Word)):
            if Selected_Word[i] == Input_Sentence:
                counter += 1
                Guess_list[i] = Input_Sentence
                Guess_Word = Guess_Word[:i] + Input_Sentence + Guess_Word[i+1:]
        if counter == 0:
            Life_Left -= 1
            print('Wrong Guess!')
            print(f'Remember You have only {Life_Left} life left')
        else:
            print('Correct!')
    else:
        print('Invalid letter!\nPlease guess one letter at a time')
        Life_Left -= 1
        print(f'Remember You have only {Life_Left} life left')
if Life_Left == 0:
    print(f'You loose!\nThe guessed word was {Selected_Word}')
else:
    print(Selected_Word)
    print('Yeh you guessed it right! You Won!')