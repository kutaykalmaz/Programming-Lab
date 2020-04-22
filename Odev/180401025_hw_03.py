"""

Olayın gerçekleşme olasılığı -> p = 0.58
Örneklem Uzay -> n = 50
Örnek olay sayısı -> k = 10
Olayın gerçekleşme olasılığı p=0.58 olan bir örnek olayın n=50 kez gerçekleştiğinde k=10 kez gerçekleşme olasılığının binom dağılım grafiği

Kutay Kalmaz  180401025

"""

from sympy import *
import matplotlib.pyplot as plt

x, n, p, k = Symbol('x'), Symbol('n'), Symbol('p'), Symbol('k')
f = binomial(n, k) * p ** k * (1 - p) ** (n - k)
# SymPy kütüphanesi ile
plot(f.subs({p: 0.58, k: 10}), (n, 1, 50), title="Binomial Distribution Graph")
# For ve Klasik matplotlib.pyplot kütüphanesi ile
xDegerleri, yDegerleri = [], []
for i in range(1, 50):
    y = f.subs({p: 0.58, k: 10, n: i})
    xDegerleri.append(i)
    yDegerleri.append(y)
plt.plot(xDegerleri, yDegerleri)
plt.show()
