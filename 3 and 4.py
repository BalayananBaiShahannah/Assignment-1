#3 and #4
import numpy as np 
import matplotlib.pyplot as plt

def equation3(x):
    return x**10 - x**8 + x**2 - 8
def equation4(x):
    return x**4 + x**3 + x**2 + x + 1

x = np.linspace(-2, 2, 100)

y3 = equation3(x)
y4 = equation4(x)

plt.plot(x, y3, label="x^10 - x^8 + x^2 - 8")
plt.plot(x, y4, label="x^4 + x^3 + x^2 + x + 1")
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Equations')
plt.legend()

plt.grid(True)
plt.show()