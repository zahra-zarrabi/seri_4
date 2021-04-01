import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
# a*x**3+b*x**2+c*x+d=0

x = []
u=[1, (-1+(-3**(1/2)))/2, ((-1+(-3**(1/2)))/2)**2]
w = (18 * a * b * c * d) - (4 * (b**3) * d) + ((b**2) * (c**2)) - (4 * a * (c**3)) - (27 * (a**2) * (d**2))
d_0=(b**2)-(3*a*c)
d_1=2*(b**3) - 9*a*b*c + 27*(a**2)*d
p=(-27*(a**2)*w)**(1/2)
p = (d_1**2)-4*(d_0**3)
p = p**(1/2)
C=((d_1-p)/2)**(1/3)
for m in range(3):
    x.append((-1/(3*a))*(b+C*u[m]+(d_0/(C*u[m]))))
print(x)










