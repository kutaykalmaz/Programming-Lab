import sympy
import math
from sympy import Symbol, solve, sin, Limit, S, oo

theta = Symbol('theta')
# math.sin(theta)


print(sympy.sin(theta)*sympy.sin(theta))

u = Symbol('u')
t = Symbol('t')
g = Symbol('g')

print(solve(u*sin(theta)-g*t, t))

x = Symbol('x')
l = Limit(1/x, x, oo)
print(l.doit())

st = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')

st1 = st.subs({t: t1})
st1_delta = (st.subs({t: t1+delta_t}))
f_d = Limit(((st1_delta - st1) / delta_t), delta_t, 0)
print(f_d.doit())
