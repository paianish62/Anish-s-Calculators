x = int(input('enter no.'))
c = 1

if x == 1:
    print('The factorial is 1')
elif x == 0:
    print('The factorial is 1')
elif x > 1 :
    for i in range(1,x+1):
        c = c * i
        
print(c)        

