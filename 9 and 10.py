#9 and #10
import numpy as np 
import matplotlib.pyplot as plt

def equation9(x):
    return (x**3/2*x) - 10*x
def equation10(x):
    return (x + 2)*(x + 3)*(x - 4)

x = np.linspace(-20, 20, 200)

y9 = equation9(x)
y10 = equation10(x)

plt.plot(x, y9, label="(x^3/2 x) - 10 x)")
plt.plot(x, y10, label="(x + 2)*(x + 3)*(x - 4)")
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Equations')
plt.legend()

plt.grid(True)
plt.show()