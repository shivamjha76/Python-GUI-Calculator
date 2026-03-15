from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("455x500")
root.configure(bg="gray")

screen_value = StringVar()
screen_value.set("")

def click(event):
    global screen_value
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            value= eval(screen_value.get())
            
        screen_value.set(value)
        screen.update()
        
    elif text == "c":
        screen_value.set("")
        screen.update()
    

    elif text == "⌫":
        screen_value.set(screen_value.get()[:-1]) 
        screen.update() 
    elif text == "x":
        screen_value.set(screen_value.get()+ "*")
    else:
        screen_value.set(screen_value.get() + text)
        screen.update()

screen = Entry(root,textvar=screen_value, font="arial 30", relief="sunken", borderwidth=5,)
screen.grid(row=0, column=0, columnspan=4, pady=(0,10))

# -------------------First row ------------------------- #
button = Button(root, text="c", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=1, column=0)
button.bind("<Button-1>", click)

button = Button(root, text="⌫", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=1, column=1)
button.bind("<Button-1>", click)

button = Button(root, text="%", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=1, column=2)
button.bind("<Button-1>", click)

button = Button(root, text="/", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=1, column=3)
button.bind("<Button-1>", click)

# ------------------------ Second row ------------------------ #
button = Button(root, text="7", font="arial 30", height=1, width=4, relief="raised", borderwidth=5,)
button.grid(row=2, column=0)
button.bind("<Button-1>", click)

button = Button(root, text="8", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=2, column=1)
button.bind("<Button-1>", click)

button = Button(root, text="9", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=2, column=2)
button.bind("<Button-1>", click)

button = Button(root, text="x", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=2, column=3)
button.bind("<Button-1>", click)

# ----------------------- Third row -------------------- #
button = Button(root, text="4", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=3, column=0)
button.bind("<Button-1>", click)

button = Button(root, text="5", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=3, column=1)
button.bind("<Button-1>", click)

button = Button(root, text="6", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=3, column=2)
button.bind("<Button-1>", click)

button = Button(root, text="-", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=3, column=3)
button.bind("<Button-1>", click)

# ---------------------- Fourth row -------------------- #
button = Button(root, text="1", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=4, column=0)
button.bind("<Button-1>", click)

button = Button(root, text="2", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=4, column=1)
button.bind("<Button-1>", click)

button = Button(root, text="3", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=4, column=2)
button.bind("<Button-1>", click)

button = Button(root, text="+", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=4, column=3)
button.bind("<Button-1>", click)

# ---------------------- fifth row ------------------------- #
button = Button(root, text="s", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=5, column=0)
button.bind("<Button-1>", click)

button = Button(root, text="0", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=5, column=1)
button.bind("<Button-1>", click)

button = Button(root, text=".", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=5, column=2)
button.bind("<Button-1>", click)

button = Button(root, text="=", font="arial 30", height=1, width=4, relief="raised", borderwidth=5)
button.grid(row=5, column=3)
button.bind("<Button-1>", click)

root.mainloop()
