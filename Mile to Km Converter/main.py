import tkinter
window = tkinter.Tk()
# window.title('My GUI Programe')
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
# mylabel = tkinter.Label(text='Its a Label', font=('Arial', 24, 'bold'))
# mylabel.grid(row=0, column=0)
# def button_click():
#     mylabel.config(text=blankSpace.get())
# blankSpace = tkinter.Entry()
# blankSpace.grid(row=2, column=3)
# button = tkinter.Button(text='Submit', command=button_click)
# button.grid(row=1, column=1)
# newbuttom = tkinter.Button(text='New Button', command=button_click)
# newbuttom.grid(row=0, column=2)
window.title('Mile To KM')
window.config(padx=30, pady=30)
Mileinput = tkinter.Entry()
Mileinput.grid(row=0, column=1)
Milelabel = tkinter.Label(text='Miles')
Milelabel.grid(row=0, column=2)
Equallabel = tkinter.Label()
Equallabel.config(text='is equal to')
Equallabel.grid(row=1, column=0)
def convert():
    "'Convert Mile into Kilo Metre'"
    mile = float(Mileinput.get())
    Km = round(mile*1.609, 2)
    Kmval.config(text=str(Km))
Kmval = tkinter.Label()
Kmval.config(text=0)
Kmval.grid(row=1, column=1)
Km = tkinter.Label()
Km.config(text='KM')
Km.grid(row=1, column=2)
butonn = tkinter.Button()
butonn.config(text='Calculate', command=convert)
butonn.grid(row=2, column=1)

window.mainloop()