import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def f(x,a,b,c):
    return a*x**2+b*x+c



def plot_graph():
    global canvas
    
    # Daten für den Plot
    #value_x = eingabe.get() 
    value_x = slider_intervall.get() # holt die Daten vom Slider
    value_a = slider_a.get()
    value_b = slider_b.get()
    value_c = slider_c.get()

    x = [i/10 for i in range(-int(value_x),int(value_x))]
    y = [f(i/10,value_a,value_b,value_c) for i in range(-int(value_x),int(value_x))]
  

    # Erstellen des Plots
    fig = plt.figure(figsize=(4, 4))
    plt.plot(x, y)
    plt.xlabel(f'f(x)={value_a}*x^2+{value_b}*x+{value_c}')
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
#root.geometry("500x500")




# Eingabe welcher Bereich angezeigt werden soll und der Label dazu
intervall = tk.Label(root,text="Gib  die größe des Intervalls ein x in [-a,a]")
intervall.pack()

eingabe = tk.Entry(root,width=200)
eingabe.pack()


# Schieberegler erstellen für das Intervall
slider_intervall = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,label="x-Intervall")
slider_intervall.pack()


# Schieberegler erstellen für a
slider_a = tk.Scale(root, from_=-100, to=100, orient=tk.HORIZONTAL)
slider_a.pack()


# Schieberegler erstellen für b
slider_b = tk.Scale(root, from_=-100, to=100, orient=tk.HORIZONTAL)
slider_b.pack()


# Schieberegler erstellen für c
slider_c = tk.Scale(root, from_=-100, to=100, orient=tk.HORIZONTAL)
slider_c.pack()






# Button zum Anzeigen des Plots
plot_button = tk.Button(root, text="Plot anzeigen", command=plot_graph)
plot_button.pack()

# Beenden Button
quit_button = tk.Button(root,text="Beenden",command=root.quit)
quit_button.pack()

# Tkinter-Fenster starten
root.mainloop()
