from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
tomato_img = PhotoImage(file = "tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column = 1)

header = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW,)
header.grid(row = 0, column = 1)

start_button = Button(text = "start", highlightthickness=0)
start_button.grid(row=3, column = 0)

reset_button = Button(text = "reset", highlightthickness=0)
reset_button.grid(row=3, column=2)

check_marks = Label(text="✔", fg = GREEN, bg=YELLOW)
check_marks.grid(row=4, column = 1)


window.mainloop()
