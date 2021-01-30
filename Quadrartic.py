x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = int(input("Enter Third number "))
v = int(input("Enter fourth number "))
a = y - x
s = z - y
d = v - z
#First Digits
p = x - a
#First Digit Functionality
q = s - a
e = d - s
#Second Digits
u = q/2
po = e/2
t = x - (1*u)
f = y - (4*u)
aa = z - (9*u)
o = f - t
j = (o*2)+(u*4)
jk = y - j
i = jk
#Second Digits Functionality
#Rememeber - and - is equal to plus
if a >(-1) and a == s and s == d:
#The greater than and smaller than signs are to check wether the integer is positive or negative
    print("{}n+{}".format(a,p))
elif a <(0) and a == s and s == d:
    print("{}n+{}".format(a,p))
elif i >(-1) and e == q and o >(-1):
    print("{}n²+({}n+{})".format(u,o,i))
elif i >(-1) and e == q and o <(0):
    print("{}n²+({}n+{})".format(u,o,i))
elif i <(0) and e == q and o <(0):
    print("{}n²({}n{})".format(u,o,i))
elif i <(0) and e == q and o >(-1):
    print("{}n²({}n+{})".format(u,o,i))
