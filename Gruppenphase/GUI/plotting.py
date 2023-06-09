import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def f(x):
    return x**2
def g(x):
    return x**3

def plot_graph():
    global canvas
    
    # Daten für den Plot
    #value1 = eingabe.get() 
    value1 = slider.get() # holt die Daten vom Slider
    x = [i/10 for i in range(-int(value1),int(value1))]
    if variable.get()=="f(x)":
        y = [f(i/10) for i in range(-int(value1),int(value1))]
    else:
        y = [g(i/10) for i in range(-int(value1),int(value1))]   

    # Erstellen des Plots
    fig = plt.figure(figsize=(4, 4))
    plt.plot(x, y)
    plt.grid()

    if 'canvas' in globals():
        canvas.get_tk_widget().destroy()
    # Erstellen des FigureCanvasTkAgg-Widgets
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    # Anzeigen des Plots in Tkinter
    canvas.get_tk_widget().pack()

# Tkinter-Fenster erstellen
root = tk.Tk()
root.geometry("500x500")


# Welche Funktion 
variable = tk.StringVar(root)
variable.set("f(x)")
functions = tk.OptionMenu(root,variable,"f(x)","g(x)",command=plot_graph)
functions.pack()


# Label der Funktionen
fg_x = tk.Label(root,text="f(x)=x^2 und g(x)=x^3")
fg_x.pack()

# Eingabe welcher Bereich angezeigt werden soll und der Label dazu
intervall = tk.Label(root,text="Gib  die größe des Intervalls ein x in [-a,a]")
intervall.pack( )

eingabe = tk.Entry(root,width=200)
eingabe.pack()


# Schieberegler erstellen
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.pack()
slider.bind("<ButtonRelease-1>", lambda event: plot_graph())

# Button zum Anzeigen des Plots
plot_button = tk.Button(root, text="Plot anzeigen", command=plot_graph)
plot_button.pack()

# Beenden Button
quit_button = tk.Button(root,text="Beenden",command=root.quit)
quit_button.pack()

# Tkinter-Fenster starten
root.mainloop()
