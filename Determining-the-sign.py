import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

a = int(input("meghdar \"x²\" ra vared konid =>"))
b = int(input("meghdar \"x\" ra vared konid =>"))
c = int(input("meghdar \"c\" ra vared konid =>"))

x = symbols('x')

equat = Eq(a * x**2 + b * x + c, 0)

root = solve(equat, x)
print("rishe haye moadele", root)

def equation(x):
    return a * x**2 + b * x + c
x_values = np.linspace(-50, 50, 20000)
y_values = equation(x_values)

signs = np.sign(y_values)

roots = np.where(np.diff(signs))[0]

print("baze mosbat va manfi moadele:")
for i in range(len(roots) + 1):
    if i == 0:
        start = x_values[0]
        end = x_values[roots[i]]
    elif i == len(roots):
        start = x_values[roots[i - 1]]
        end = x_values[-1]
    else:
        start = x_values[roots[i - 1]]
        end = x_values[roots[i]]

    sample_x = (start + end) / 2
    sample_y = equation(sample_x)
    sign = '+' if sample_y > 0 else '-'

    print(f"baze [{start:.2f}, {end:.2f}]: {sign}")
    

plt.plot(x_values, y_values, label=f'y = {a}x² + {b}x + {c}')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Determining the sign')
plt.legend()
plt.grid(True)
plt.show()

