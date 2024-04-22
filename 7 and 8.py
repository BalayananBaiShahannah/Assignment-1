#7 and #8
import numpy as np 
import matplotlib.pyplot as plt

def equation7(x):
    return x**3 + 2*x**2 - 10*x + 3
def equation8(x):
    return np.cos(x)/(5*x)

x = np.linspace(-2, 2, 100)

y7 = equation7(x)
y8 = equation8(x)

plt.plot(x, y7, label="x^3 + 2 x^2 - 10 x + 3")
plt.plot(x, y8, label="cos(x)/(5*x)")
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Equations')
plt.legend()

plt.grid(True)
plt.show()