#Решатель квадратных уравнений

from math import sqrt
a = float(input())
b = float(input())
c = float(input())
x1 = int(-(b+sqrt(b**2-(4*a*c)))/(2*a))
x2 = int(-(b-sqrt(b**2-(4*a*c)))/(2*a))
print(x1)
print(x2)
