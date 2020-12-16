from tkinter import *

def click(event):
    global  scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
               value = eval(screen.get())
            except Exception as e:
                print(e)
                scvalue.set("Error")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("600x700")
root.minsize(599, 699)
root.maxsize(699, 799)
root.title("Calculator by Sam")
root.wm_iconbitmap("2.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, text=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

f = Frame(root, bg="grey")
b = Button(f, text="9",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="6",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="5",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="3",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="1",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=8, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=7, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="c",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=9, pady=5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="+",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=11, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/",padx=18,pady=12, font="lucida 35 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)
f.pack()




root.mainloop()