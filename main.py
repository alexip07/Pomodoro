import tkinter as tk
import math

# Constants used for setting the GUI

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

# TIMER MECHANISM


def reset_timer():
    global reps
    """it will reset the timer and the check marks using the button soo a new cycle could begin"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


def start_timer():

    """it has a global value used for the countdown, then it checks where is it standing with it,
    and adjust the timer accordingly"""

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long break", bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short break", bg=YELLOW, fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", bg=YELLOW, fg=GREEN)


# COUNTDOWN MECHANISM

# Countdown function
def count_down(count):
    """it checks if the seconds are less than 10 soo it can display a nice clock,
    and the second half is used for refreshing the countdown using methods from tkinter """
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=f"{mark}")


# GUI SETUP

# Window setup

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas setup
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="OO:OO", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Labels
label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW)
label.config(font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

check_mark = tk.Label(fg=GREEN, bg=YELLOW)
check_mark.config(font=24)
check_mark.grid(column=1, row=3)

# Buttons
start_button = tk.Button(text="Start", fg=PINK, bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", fg=PINK, bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
