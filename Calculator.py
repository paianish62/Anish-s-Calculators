inp = str(input('Enter your question in the fromat: a + b (this calculator only works for +,-,/,*,%) '))
x = inp.split()
terms = list(x)
#print(terms)
a = int(terms[0])
#print(tone)
c = str(terms[1])
b = int(terms[2])
#print(a*b)
c = str(terms[1])
def func(q,w,e):
    f = w
    if f == '*':
        print(q*e)
    elif f == '/':
        print(q/e)
        m = q%e
        if m > 0 :
            print('your remainder is {}'.format(m))
    elif f == '+':
        print(q+e)
    elif f == '-':
        print(q-e)
    else:
        print('An error occured')

func(a,c,b)

