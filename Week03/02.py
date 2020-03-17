from sympy import FiniteSet
from fractions import Fraction

t = FiniteSet(1, 2, 3)
s = FiniteSet(2, 4, 6)

if t == s:
    print("True")
else:
    print("False")

print(t.union(s))
print(t.intersect(s))
print(t**2)


def probability(space, event):
    return len(event) / len(space)


def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True


space = FiniteSet(* range(1, 21))
primes = []
for num in space:
    if check_prime(num):
        primes.append(num)

event = FiniteSet(* primes)
p = probability(space, event)

print("Sample space: ", space)
print("Event: ", event)
print('Probability of event: {0:.3f}'.format(p))
