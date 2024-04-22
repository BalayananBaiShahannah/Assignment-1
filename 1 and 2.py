#1 and #2
import numpy as np 
import matplotlib.pyplot as plt

def equation1(x):
    return x**2 - 10
def equation2(x):
    return x**3 + x - 100

x = np.linspace(-20, 20, 200)

y1 = equation1(x)
y2 = equation2(x)

plt.plot(x, y1, label="x^2 - 10")
plt.plot(x, y2, label="x^3 + x - 100")
plt.axhline(y=0, color='y')
plt.axvline(x=0, color='y')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting Equations')
plt.legend()

plt.grid(True)
plt.show()