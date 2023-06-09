import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**2 - x*2 + 2) / (x - 1)

x_1 = np.linspace(1.1, 10, num=1000)
x_2 = np.linspace(0.9, -10, num=1000)

plt.plot(x_1, f(x_1), label='f(x) für x > 1')
plt.plot(x_2, f(x_2), label='f(x) für x < 1')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot von f(x)')
plt.grid(True)
plt.show()
