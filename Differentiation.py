s = str(input('what type of differentiation you want to do? (Simple) '))
def dif(k,x,n):
    Ans = k*n*x
    Ans2 = k*n
    power = n - 1
    if x != "x":
        x = int(x)
        res = ('{}^{}'.format(Ans,power))
    else:
        res = ('{}{}^{}'.format(Ans2,x,power))
    print(res)
if s =='Simple':
    vk = int(input('enter k '))
    vx = str(input('enter x '))
    vn = int(input('enter n '))

dif(vk,vx,vn)
    



