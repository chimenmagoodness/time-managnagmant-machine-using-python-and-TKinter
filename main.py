import math
from tkinter import *

# ---------------------------------------------------------------CONSTANT-----------------------------------------------
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


# --------------------------------------------------------------- TIMER RESET-------------------------------------------
def reset_timer():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    title_text.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# --------------------------------------------------------------- TIMER MECHANISM --------------------------------------
def star_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_text.config(text="LongBreak", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_text.config(text="ShortBreak", fg=PINK)
    else:
        count_down(work_sec)
        title_text.config(text="Work", fg=GREEN)


# --------------------------------------------------------------- COUNTDOWN MECHANISM ----------------------------------
def count_down(count):
    count_mins = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        star_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark.config(text=marks)

# --------------------------------------------------------------- UI SETUP ---------------------------------------------


window = Tk()


window.title("Pomodoro")
window.config(padx=100, pady=50,  bg=YELLOW)

canvas = Canvas(width=440, height=440, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(220, 230, image=img)
timer_text = canvas.create_text(220, 250, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_text.grid(column=1, row=0)

# Buttons
start_btn1 = Button(text="Start", highlightthickness=0, command=star_timer)
start_btn1.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Checkbox
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()
