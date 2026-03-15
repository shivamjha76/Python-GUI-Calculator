from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("350x450")
root.configure(bg="#1e1e1e")

screen_value = StringVar()
screen_value.set("0")

# ---------------- CLICK FUNCTION ---------------- #

def click(event=None, text=None):

    if text is None:
        text = event.widget.cget("text")

    if text == "=":
        try:
            expression = screen_value.get().replace("x","*")
            result = eval(expression)
            screen_value.set(result)
        except:
            screen_value.set("Error")

    elif text == "C":
        screen_value.set("")

    elif text == "⌫":
        screen_value.set(screen_value.get()[:-1])

    else:
        screen_value.set(screen_value.get() + text)


# ---------------- SCREEN ---------------- #

screen = Entry(
    root,
    textvar=screen_value,
    font=("Arial",35),
    justify="right",
    bg="#1e1e1e",
    fg="white",
    borderwidth=0
)

screen.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=10)

# ---------------- BUTTON FUNCTION ---------------- #

def create_button(text,row,col,width=1):

    if text in ["+","-","x","/","="]:
        bg = "#ff9500"
    elif text in ["C","⌫"]:
        bg = "#a5a5a5"
    else:
        bg = "#333333"

    button = Button(
        root,
        text=text,
        font=("Arial",20,"bold"),
        bg=bg,
        fg="white",
        relief="flat",
        activebackground="#555"
    )

    button.grid(
        row=row,
        column=col,
        columnspan=width,
        sticky="nsew",
        padx=5,
        pady=5
    )

    button.bind("<Button-1>", click)


# ---------------- BUTTON LAYOUT ---------------- #

buttons = [
["C","⌫","%","/"],
["7","8","9","x"],
["4","5","6","-"],
["1","2","3","+"],
["0",".","00","="]
]

for r,row in enumerate(buttons):
    for c,text in enumerate(row):

        if text == "0":
            create_button(text,r+1,c,)   # double width
        else:
            create_button(text,r+1,c)


# ---------------- GRID EXPANSION ---------------- #

for i in range(5):
    root.grid_rowconfigure(i,weight=1)

for i in range(4):
    root.grid_columnconfigure(i,weight=1)


# ---------------- KEYBOARD SUPPORT ---------------- #

def key_input(event):
    key = event.char

    if key in "0123456789+-*/.%":
        click(text=key)

    elif event.keysym == "Return":
        click(text="=")

    elif event.keysym == "BackSpace":
        click(text="⌫")

root.bind("<Key>",key_input)

root.mainloop()
