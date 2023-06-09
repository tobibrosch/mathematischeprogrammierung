import tkinter as tk

def button_clicked():
    label.config(text="Halt")

def button_clicked2():
    label2.config(text="die Backen")

# Erstellen des Hauptfensters
window = tk.Tk()

# Festlegen des Fenstertitels
window.title("Meine GUI-Anwendung")

# Erstellen eines Labels
label = tk.Label(window,text="Hallo")
label.pack()
label2 = tk.Label(window, text="Willkommen zur GUI-Anwendung")
label2.pack()
# Erstellen eines Buttons
button1 = tk.Button(window, text="Klick mich!", command=button_clicked)
button1.pack()

button = tk.Button(window, text="Klick mich nochmal!", command=button_clicked2)
button.pack()

# Starten der GUI-Schleife
window.mainloop()