import math
x = input('Enter Type of Triangle (Regular or Right) ')
def Conv(a):
    A = (a*math.pi)/180
    return A
def sines(ao,so,st):
    print(math)
    L = math.asin((math.sin(Conv(ao))*st)/so)
    
    K = ((L*180)/math.pi)
    return K
#c2 = a2 + b2 − 2ab cos(C)
def cosine(a,b,c):
    D = (a*a)+(b*b)-((2*a*b)*(math.cos(Conv(c))))
    G = math.sqrt(D)
    return G
def trig(): 
    if x.lower() == 'right':
        y = input('Enter Sin, Cos or Tan or enter Info to learn more about these angles ')
        if y.lower() =='info':
            print('Sin(θ) = Opp/Hyp, Cos(θ) = Adj/Hyp, Tan(θ) = Opp/Adj')
            trig()
        elif y.lower() == 'sin':
            t = input('enter what you want to find (Opp or Hyp) ')
            if t.lower() == 'opp':
                Hyp = int(input('Enter Hypotnuse ' ))
                Angl = int(input('Enter Known Angle '))
                print((math.sin(Conv(Angl))*Hyp))
            elif t.lower() == 'hyp':
                Hyp = int(input('Enter Opposite ' ))
                Angl = int(input('Enter Known Angle '))
                k = (math.sin(Conv(Angl)))
                print(Hyp/k)
        elif y.lower() == 'cos':
            t = input('enter what you want to find (Adj or Hyp) ')
            if t.lower() == 'adj':
                Hyp = int(input('Enter Hypotnuse ' ))
                Angl = int(input('Enter Known Angle '))
                print((math.cos(Conv(Angl))*Hyp))
            elif t.lower() == 'hyp':
                Hyp = int(input('Enter Adjacent ' ))
                Angl = int(input('Enter Known Angle '))
                print(Hyp/(math.cos(Conv(Angl))))
        elif y.lower() == 'tan':
            t = input('enter what you want to find (Opp or Adj) ')
            if t.lower() == 'opp':
                Hyp = int(input('Enter Hypotnuse ' ))
                Angl = int(input('Enter Known Angle '))
                print((math.tan(Conv(Angl))*Hyp))
            elif t.lower() == 'adj':
                Hyp = int(input('Enter Adjacent ' ))
                Angl = int(input('Enter Known Angle '))
                print(Hyp/(math.tan(Conv(Angl))))
    else:
        y = input('Enter sine or cosine ')
        if y == 'sine':
            angosid = str(input("Enter wethear you want to find unknow Angle or Side "))
            if angosid.lower() == "angle":
                angla=int(input('enter angle 1 '))
                a = int(input('enter side 1 '))
                b = int(input('enter side 2 '))
                print('angle 2 = {}'.format(sines(angla,a,b)))
            elif angosid.lower() == "side":
                angla=int(input('enter side 1 '))
                a = int(input('enter angle 1 '))
                b = int(input('enter angle 2 '))
                print('Side 2 = {}'.format(sines(angla,a,b)))

        elif y.lower() == 'cosine':
            c = int(input('enter known angle betweeen sides '))
            a = int(input('enter side 1 '))
            b = int(input('enter side 2 '))
            print('Side 3 is equal to {}'.format(cosine(a,b,c)))

trig()

            
    
