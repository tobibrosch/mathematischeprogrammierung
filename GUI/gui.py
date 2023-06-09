from tkinter import *
 
fenster = Tk()
fenster.geometry("300x300")
fenster.title("Umrechner")

def button_1():
    value1 = number1.get()
    value2 = number2.get()
    Sum = float(value1)+float(value2)
    my_label.config(text=f"Summe ist {Sum}")

button = Button(fenster,text="Berechne",command=button_1)
quitbutton = Button(fenster,text="Beenden",command=fenster.quit)

number1 = Entry(fenster,width=10)
number2 = Entry(fenster,width=10)

my_label = Label(fenster,text="Summe=")

label_number1 = Label(fenster,text="Zahl 1")

label_number2 = Label(fenster,text="Zahl 2")


label_number1.pack()
number1.pack()
label_number2.pack()
number2.pack()
button.pack()
my_label.pack()
quitbutton.pack()


fenster.mainloop()

