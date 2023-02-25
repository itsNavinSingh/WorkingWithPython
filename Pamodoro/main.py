import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = '✔️'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timerlabel.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Start_timer():
    global reps
    reps += 1
    if reps%2 == 1:
        countdown(WORK_MIN*60)
        timerlabel.config(text='Work', fg=GREEN)
    elif reps%8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timerlabel.config(text='Break', fg=RED)
    else:
        countdown(SHORT_BREAK_MIN*60)
        timerlabel.config(text='Break', fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    cmin = count//60
    csec = count%60
    if len(str(cmin)) == 1:
        cmin = f'0{cmin}'
    if len(str(csec)) == 1:
        csec = f'0{csec}'
    show = f'{cmin}:{csec}'
    canvas.itemconfig(timer_text, text=show)
    if count > 0:
        global timer
        timer = window.after(10, countdown, count-1)
    else:
        Start_timer()
        check_marks.config(text=CHECKMARK*(reps//2))
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('Pomodoro')
timerlabel = tkinter.Label(text='Timer', font=(FONT_NAME, 35, 'normal'), bg=YELLOW, fg=GREEN)
timerlabel.grid(row=0, column=1)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column= 1)
startbutton = tkinter.Button(text='Start', highlightthickness=0, command=Start_timer)
startbutton.grid(row=3, column=0)
resetbutton = tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
resetbutton.grid(row=3, column=2)
check_marks = tkinter.Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'normal'))
check_marks.grid(row=3, column=1)
window.mainloop()