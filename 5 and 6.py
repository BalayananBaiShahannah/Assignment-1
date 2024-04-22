#5 and #6
import numpy as np 
import matplotlib.pyplot as plt

def equation5(x):
    return (x**2 + x + 10)/2*x
def equation6(x):
    return np.sin(x)/(3*x)

x = np.linspace(-2, 2, 100)

y5 = equation5(x)
y6 = equation6(x)

plt.plot(x, y5, label="(x^2 + x + 10)/2x")
plt.plot(x, y6, label="sin(x)/(3*x)")
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Equations')
plt.legend()

plt.grid(True)
plt.show()