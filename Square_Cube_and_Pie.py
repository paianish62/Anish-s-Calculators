def cust(a,b):
        c = 0
        ans = a
        while c < (b-1) :
            ans = ans*a
            c += 1
        print(ans) 
while True :
    x = int(input("Enter No. "))
    y = str(input("Function performed on the no. (square, cube, pie or custom) "))
      
    if y == "square":
        print(x*x)
        break
    elif y == "cube":
        print(x*x*x)
        break
    elif y == "pie":
        print(x*3.14)
        break
    elif y == "custom" :
        z = int(input("Enter custom power "))
        cust(x,z)
        break
    else:
        print("please enter pie, square or custom")
