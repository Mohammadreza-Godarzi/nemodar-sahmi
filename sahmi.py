import numpy as np
import matplotlib.pyplot as plt

a = int(input("zarib \"x²\" ra vared konid =>"))
b = int(input("zarib \"x\" ra vared konid =>"))
c = int(input("zarib \"c\" ra vared konid =>"))

moadele = f"y = ({a})x² + ({b})x + ({c})"

print(f'moadele shoma : {moadele}')

delta = b**2 - 4*a*c


if delta > 0 :
    sqrt_delta = np.sqrt(delta)
    x_1 = ((-1*b) + sqrt_delta ) / (2*a)
    print(x_1)
    x_2 = ((-1*b) - sqrt_delta ) / (2*a)
    print(x_2)

    x = np.linspace(-50, 50, 400)
    y = a*x**2 + b*x + c

elif delta == 0:
    x_martabe_2 = (-1*b) / (2*a)   

    x = np.linspace(-50, 50, 400)
    y = a*x**2 + b*x + c

elif delta < 0 :
    def daraje(x):
        return a * x**2 + b*x + c

    x = np.linspace(-50, 50, 400)
    y = daraje(x)



plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'nemodare sahmi {moadele}')
plt.legend()
plt.grid(True)
plt.show()
