import tkinter
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}

window = tkinter.Tk()
window.title('Flash Card')
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
df = pd.read_csv('data/french_words.csv')
data = df.to_dict(orient='records')

def new_word():
    global selected_word, data
    selected_word = random.choice(data)
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(word, text=selected_word['French'])
    canvas.itemconfig(img, image=front_card)
    window.after(5000, func=translation)

def translation():
    global selected_word
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(word, text=selected_word['English'])
    canvas.itemconfig(img, image=back_card)

def learnt():
    global data, selected_word
    data.remove(selected_word)
    new_word()

canvas = tkinter.Canvas(width=800, height=526)
front_card = tkinter.PhotoImage(file='images/card_front.png')
back_card = tkinter.PhotoImage(file='images/card_back.png')

img = canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400, 145, text='', font=('Ariel', 48, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=3)

cancle = tkinter.PhotoImage(file='images/wrong.png')
correct = tkinter.PhotoImage(file='images/right.png')
wrong_button = tkinter.Button(image=cancle, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)
right_button = tkinter.Button(image=correct, highlightthickness=0, command=learnt)
right_button.grid(row=1, column=2)
new_word()


window.mainloop()