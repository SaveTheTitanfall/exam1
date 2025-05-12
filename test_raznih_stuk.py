"""
from math import sqrt
pi=3.141592658
d=0.0007
m0=0.00411
g=9.81
k=0.85
dd=0.000028
dm0=0.000164
dm1=2.39e-7
dm2=4.69e-7
m1p=(0.00469,0.00517,0.00550,0.00564,0.00610)
m1s=(0.00495,0.00526,0.00560,0.00609,0.00578)
n=(50.0,70.0,90.0,110.0,130.0)
otv=0
for i in range(len(m1p)):
    otv=sqrt(dm1*((g-m0*g)/(n[i]*pi*k*d))+dm0*((m1p[i]*g-g)/(n[i]*pi*k*d))+dd*((m1p[i]*g-m0*g)/(n[i]*k*pi)))
    print("otv=",otv)
    print("now")
for i in range(len(m1p)):
    otv=sqrt(dm2*((g-m0*g)/(n[i]*pi*k*d))+dm0*((m1s[i]*g-g)/(n[i]*pi*k*d))+dd*((m1s[i]*g-m0*g)/(n[i]*k*pi)))
    print("otv=",otv)
"""
from math import sqrt

pi = 3.141592658
d = 0.0007
m0 = 0.00411
g = 9.81
k = 0.85
dd = 0.000028
dm0 = 0.000164
dm1 = 2.39e-7
dm2 = 4.69e-7

m1p = (0.00469, 0.00517, 0.00550, 0.00564, 0.00610)
m1s = (0.00495, 0.00526, 0.00560, 0.00609, 0.00578)
n = (50.0, 70.0, 90.0, 110.0, 130.0)
gamasigma=0
sigmap=(0.0608,0.0794,0.081,0.073,0.0833)
sigmas=(0.088,0.0862,0.0868,0.0944,0.0674)
dsigma=0
ssigma=0
for i in range(len(m1p)):
    ssigma+=sigmap[i]
    ssigma+=sigmas[i]
ssigma=ssigma/10
print("Результаты для m1p:")
for i in range(len(m1p)):
    a1 = dm1 * (((1 - m0) * g) / (n[i] * pi * k * d))
    a2 = dm0 * (((m1p[i])*g) / (n[i] * pi * k * d))
    a3 = dd * ((m1p[i] * g - m0 * g) / (n[i] * pi * k))
    otv = sqrt(a1 + a2 + a3)
    print(f"otv[{i}] = {otv:.10f}")
    dsigma+=otv

print("\nРезультаты для m1s:")
for i in range(len(m1s)):
    a1 = dm2 * (((1 - m0) * g) / (n[i] * pi * k * d))
    a2 = dm0 * ((m1s[i] * g) / (n[i] * pi * k * d))
    a3 = dd * ((m1s[i] * g - m0 * g) / (n[i] * pi * k))
    otv = sqrt(a1 + a2 + a3)
    print(f"otv[{i}] = {otv:.10f}")
    dsigma+=otv
dsigma=dsigma/10
gamasigma=dsigma/ssigma
print(f"gamasigma = {gamasigma:.10f}")
print(f"dsigma = {dsigma:.10f}")
print(f"ssigma = {ssigma:.10f}")
