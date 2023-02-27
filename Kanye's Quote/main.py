import tkinter
import requests
def getQuote():
    kquotes = requests.get(url='https://api.kanye.rest')
    quotes = kquotes.json()['quote']
    canvas.itemconfig(show_quote, text=quotes)

window = tkinter.Tk()
window.title("Kanye's Quote")
window.config(padx=20, pady=20)
bgimage = tkinter.PhotoImage(file='background.png')
canvas = tkinter.Canvas(width=300, height=414)
canvas.create_image(150, 207, image=bgimage)
show_quote = canvas.create_text(150, 207, text='', width=250, font=('Arial', 20, 'normal'), fill='red')
canvas.grid(row=0, column=0)
face_img = tkinter.PhotoImage(file='kanye.png')
face_button = tkinter.Button(image=face_img, highlightthickness=0, command=getQuote)
face_button.grid(row=1, column=0)
getQuote()
window.mainloop()