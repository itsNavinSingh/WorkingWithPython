import tkinter
import api
import time
ScoreCard = 0
THEME_COLOR = "#375362"
ANS = True
def q_pallet():
    global ANS
    qna = api.qna()
    canvas.itemconfig(Question, text=f"{qna['Question']}")
    if qna['Answer'] == 'True':
        ANS = True
    else:
        ANS = False
    canvas.configure(background='white')


def click_right():
    global ScoreCard, ANS
    if ANS == True:
        ScoreCard += 1
        canv_color = 'green'
    else:
        canv_color = 'red'
    canvas.configure(background=canv_color)
    score.config(text=f'Score: {ScoreCard}')

def click_wrong():
    canvas.configure(background="green")
    global ScoreCard, ANS
    if ANS == False:
        ScoreCard += 1
        canv_color = 'green'
    else:
        canv_color = 'red'
    canvas.configure(background=canv_color)
    score.config(text=f'Score: {ScoreCard}')


window = tkinter.Tk()
window.title('Quizzler')
window.config(padx=10, pady=10, bg=THEME_COLOR)
score = tkinter.Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 20, 'bold'))
score.grid(row=0, column=0, columnspan=3)
canvas = tkinter.Canvas(width=400, height=400)
canvas.configure(background='white')
Question = canvas.create_text(200, 200, text='Quesion', width=350, font=('Arial', 20, 'normal'), fill='black')
canvas.grid(row=1, column=0, columnspan=3)
true_img = tkinter.PhotoImage(file='images/true.png')
false_img = tkinter.PhotoImage(file='images/false.png')
right_button = tkinter.Button(image=true_img, highlightthickness=0, command=click_right)
right_button.grid(row=3, column=2)
wrong_button = tkinter.Button(image=false_img, highlightthickness=0, command=click_wrong)
wrong_button.grid(row=3, column=0)
next_button = tkinter.Button(text='Next', highlightthickness=0, font=('Arial', 20, 'bold'), command=q_pallet)
next_button.grid(row=3, column=1)
q_pallet()
window.mainloop()