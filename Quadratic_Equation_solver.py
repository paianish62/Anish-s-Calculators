#Quadratic Equation Calculator
from math import sqrt
what = str(input('Enter 1 or 2 (1 = sovle a qudratic equation, 2 = display it in completed square format) '))
z = int(input('enter a '))
x = int(input('enter b '))
s = int(input('enter c '))
if what == '1':   
    def eqformula(a,b,c):
        z = ((-1*b)+(sqrt((b*b)-(4*a*c))))/(2*a)
        k = ((-1*b)-(sqrt((b*b)-(4*a*c))))/(2*a)
        print('your roots are {} and {}'.format(z,k))

    def check(a,b,c):
        a = (b*b)-(4*a*c)
        return a

    q = check(z,x,s)

    if q > 0 :
        eqformula(z,x,s)
    elif q < 0:
        print('your parabola has no y-intercepts')
    elif q == 0:
        l = ((-1*x)+ 0)/(2*z)
        print('your y-intercept is {}'.format(l))

elif what == '2':
    div = z/2

    if div == 0.5:
        tri = x/2
        cal = ((tri*tri)*-1)+s
        if tri > 0 and cal > 0:
            print('(x + {})^2 + {}'.format(tri,cal))
        elif tri < 0 and cal < 0:
            print('(x - {})^2 {}'.format(tri,cal))
        elif tri > 0 and cal < 0:
            print('(x + {})^2 {}'.format(tri,cal))
        elif tri < 0 and cal > 0:
            print('(x - {})^2 + {}'.format(tri,cal))
        else:
            print('an error occured, pls make sure you have entered the correct values')
    




