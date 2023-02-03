# При помощи библиотеки numpy, создать программу, интерполирующую
# экспериментальные данные и вычислить значение концентрации
# в моменты времени t1 = 1,5 и t2 = 2,5.

import numpy as np
import matplotlib.pyplot as plt

t = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
c = [0.0, 2.011, 3.349, 6.649, 16.162, 40.063, 91.758]

polynom = np.polyfit(t, c, deg=6)
print("Polynomial coefficients: ", polynom.tolist())

interpoly = np.polyval(polynom, t)
print("Interpolation coefficients: ", interpoly.tolist())

print("t = 1.5, concentration =", np.polyval(polynom, 1.5))
print("t = 2.5, concentration =", np.polyval(polynom, 2.5))

plt.subplot(221)
plt.title('Data')
plt.plot(t, c)

plt.subplot(222)
plt.title('Interpolate')
plt.plot(t, interpoly)

plt.subplot(212)
plt.title('Union')
plt.plot(t, c, label='Data')
plt.plot(t, interpoly, label='Interpolate')
plt.legend()

plt.tight_layout()
plt.show()

# Построить кривые изменения концентрации компонентов приведённой реакции во временном интервале от 0 до 175
# Описать изменение концентраций можно при помощи системы дифф. уравнений
# В исходной смеси 5% R и 95% A. 
# k1 = 0,05 k2 = 0,01.

# s0 = ca
# s1 = cr 
# s2 = cb 

from scipy.integrate import odeint

def diff(s, t):
    k1 = 0.05
    k2 = 0.01

    dcadt = -k1*s[0]
    dcrdt = k1*s[0] - k2*s[2]
    dcbdt = k2*s[1]

    return [dcadt, dcrdt, dcbdt]

t = np.linspace(0, 175, 176)
print(t)
start = [0.95, 0.05, 0]
s = odeint(diff, start, t)
print(s)
plt.plot(t, s[:,0], label='ca(t)')
plt.plot(t, s[:,1], label='cr(t)')
plt.plot(t, s[:,2], label='cb(t)')
plt.legend()
plt.show()
