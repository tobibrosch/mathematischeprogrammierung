import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import cos, tan, pi
import numpy as np
from scipy.optimize import bisect

def f(x, phi_b, v, g=9.81):
    return x * tan(phi_b) - (g * x ** 2) / (2 * v ** 2 * (cos(phi_b)) ** 2)

def plot_graph():
    global canvas

    # Daten für den Plot
    value_x = slider_intervall.get()
    value_phi = slider_phi.get()
    value_v_0 = slider_v_0.get()

    x = [i / 10 for i in range(int(value_x) * 10)]
    y = [f(i / 10, value_phi * pi / 180, value_v_0) for i in range(int(value_x) * 10)]
  
    # Nullstelle berechnen
    def calculate_nullstellen(x):
        phi_b = value_phi * pi / 180
        v = value_v_0
        g = 9.81
        def g_func(x):
            return x * tan(phi_b) - (g * x ** 2) / (2 * v ** 2 * (cos(phi_b)) ** 2)
        root = bisect(g_func, 1, 1000)
        return root

    root = calculate_nullstellen(x)

    # Erstellen des Plots
    fig = plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.xlabel(f'Flugweite in m bei v_0={value_v_0} m/s und phi = {value_phi} Grad, max. Weite {round(root, 2)} Meter')
    plt.ylabel(f'Flughöhe (max. Höhe {round(max(y), 2)} Meter)')
    plt.ylim(0, np.max(y) + 0.1)
    plt.grid()

    num_ticks = 11  # Anzahl der Striche
    x_ticks = np.linspace(min(x), max(x), num_ticks)
    plt.xticks(x_ticks)


    if 'canvas' in globals():
        canvas.get_tk_widget().destroy()
    # Erstellen des FigureCanvasTkAgg-Widgets
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    # Anzeigen des Plots in Tkinter
    canvas.get_tk_widget().pack()


# Tkinter-Fenster erstellen
window = tk.Tk()
window.geometry("800x600")
window.title("Flugkurve")

# Frame für Schieberegler
slider_frame = tk.Frame(window)
slider_frame.pack(pady=20)

# Schieberegler erstellen für das Intervall
slider_intervall = tk.Scale(slider_frame, from_=0, to=1000, resolution=10, length=300,
                            orient=tk.HORIZONTAL, label="x-Intervall")
slider_intervall.pack(side=tk.LEFT, padx=10)
slider_intervall.set(100)
slider_intervall.bind("<ButtonRelease-1>", lambda event: plot_graph())

# Schieberegler erstellen für phi
slider_phi = tk.Scale(slider_frame, from_=0.1, to=89.9, resolution=0.1, length=300,
                      orient=tk.HORIZONTAL, label="Abwurfwinkel")
slider_phi.pack(side=tk.LEFT, padx=10)
slider_phi.set(10)
slider_phi.bind("<ButtonRelease-1>", lambda event: plot_graph())

# Schieberegler erstellen für v_0
slider_v_0 = tk.Scale(slider_frame, from_=0, to=100, resolution=0.1, length=300,
                      orient=tk.HORIZONTAL, label="Abwurfgeschwindigkeit")
slider_v_0.pack(side=tk.LEFT, padx=10)
slider_v_0.set(10)
slider_v_0.bind("<ButtonRelease-1>", lambda event: plot_graph())

# Button zum Anzeigen des Plots
plot_button = tk.Button(window, text="Plot anzeigen", command=plot_graph)
plot_button.pack(pady=10)

# Beenden Button
quit_button = tk.Button(window, text="Beenden", command=window.quit)
quit_button.pack(pady=10)

# Tkinter-Fenster starten
window.mainloop()
