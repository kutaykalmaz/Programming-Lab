from sympy import Symbol, pprint
import sympy as sym
import matplotlib.pyplot as plt

p = Symbol('p')
x = Symbol('x')
n = Symbol('n')

my_f_3_part_0 = sym.factorial(n) / (sym.factorial(x) * sym.factorial(n - x))
print(my_f_3_part_0)

my_f_3_part_1 = p ** x
print(my_f_3_part_1)

my_f_3_part_2 = (1 - p) ** (n - x)
print(my_f_3_part_2)

my_f_3 = my_f_3_part_0 * my_f_3_part_1 * my_f_3_part_2
print(my_f_3)

sym.plot(my_f_3.subs({p: 0.5, n: 50}), (x, 0, 50), title="Binomal distribution plot for n=50")
sym.show()

x_value = []
y_value = []
for value in range(50):
    y = my_f_3.subs({p: 0.5, n: 50, x: value}).evalf()
    y_value.append(y)
    x_value.append(value)
plt.plot(x_value, y_value)
plt.show()
