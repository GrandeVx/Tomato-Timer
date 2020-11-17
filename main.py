from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
Title = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    windows.after_cancel(timer)
    reps = 0
    title.config(text="Timer",fg=GREEN,font=(FONT_NAME,53),bg=YELLOW)
    Canvas.itemconfig(timer_text,text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# Function for Call the Countdown Function With the Parameter
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        Countdown(LONG_BREAK_MIN*60)
        title.config(text="Break",fg=RED,font=(FONT_NAME,53),bg=YELLOW)
    elif reps % 2 == 0:
        Countdown(SHORT_BREAK_MIN*60)
        title.config(text="Break",fg=RED,font=(FONT_NAME,53),bg=YELLOW)
    else:
         Countdown(WORK_MIN*60)
         title.config(text="Work",fg=GREEN,font=(FONT_NAME,53),bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def Countdown(count):

    minute = math.floor(count / 60)
    second = count % 60
    
    if minute < 10:
        minute = f"0{minute}"
    
    if int(second) < 10:
        second = f"0{second}"

    if second == 0:
        second = "00"

    Canvas.itemconfig(timer_text,text=f"{minute}:{second}")


    if count > 0:
        global timer
        timer = windows.after(1000,Countdown,count - 1)
    else:
        start_timer()
        check.config(text=check["text"]+"✔")
# ---------------------------- UI SETUP ------------------------------- #

# Windows Setup
windows = Tk()
windows.title("Pomodoro Timer")
windows.geometry("500x600")
windows.resizable(width=False, height=False)
windows.config(padx=80,pady=100,bg=YELLOW)



# Title 
title = Label()
title["text"]= "Timer"
title.config(fg=GREEN,font=(FONT_NAME,53),bg=YELLOW)
title.grid(column=1,row=0)


# Background Tomato with Timer
Canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
foto = PhotoImage(file="tomato.png")
Canvas.create_image(103,112,image=foto)
timer_text = Canvas.create_text(103,117,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
Canvas.grid(column=1,row=1)

# Start Button
start = Button(highlightbackground=YELLOW,command=start_timer)
start["text"]="Start"
start.grid(column=0,row=3)

# Reset Button
reset = Button(highlightbackground=YELLOW,command=reset_timer)
reset["text"] = "Reset"
reset.grid(column=3,row=3)

# Check Icon
check = Label(text="✔",fg=GREEN,bg=YELLOW)
check.grid(column=1,row=4)

# main Loop
windows.mainloop()