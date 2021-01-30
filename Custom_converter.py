



while True:
    typ = str(input('what do you want to convert (mass , currency , lenght) '))
    
    
    if typ == 'over':
        print('thankyou for using our calculator')
        break
    else:
       
        
        if typ == 'mass':
            while True:
                way = int(input('Enter option no. ( 1: Kg -> lb, 2: lb -> Kg, 3: Kg -> g, 4: lb -> g, 5: Change category, 6: Exit) '))
                
                if way == 1:
                    val = int(input('enter your value to be converted '))
                    print('{} Kg is equal to {} lb'.format(val,val*2.20462262))
                elif way == 2:
                    val = int(input('enter your value to be converted '))
                    print('{} lb is equal to {} kg'.format(val,val/2.20462262))
                elif way == 3:
                    val = int(input('enter your value to be converted '))
                    print('{} kg is equal to {} g'.format(val,val*1000))
                elif way == 4:
                    val = int(input('enter your value to be converted '))
                    print('{} lb is equal to {} g'.format(val,val/0.00220462))
                elif way == 5:
                    print('changing category...')
                    break
                elif way == 6:
                    print('thankyou for using our calculator')
                    exit()
                else:
                    
                    print('pls enter a valid option')
                    continue
                    
            
        elif typ == 'lenght':
            while True:
                way = int(input('Enter option no. (1: M -> Km, 2: Km -> M, 3: M -> ft, 4: M -> in, 5: Change category, 6: Exit) '))
                
                if way == 1:
                    val = int(input('enter your value to be converted '))
                    print('{} M is equal to {} Km'.format(val, val/0.62137119))
                elif way == 2 :
                    val = int(input('enter your value to be converted '))
                    print('{} Km is equal to {} M'.format(val, val*0.62137119))
                elif way == 3 :
                    val = int(input('enter your value to be converted '))
                    print('{} M is equal to {} ft'.format(val, val/0.00018939))
                elif way == 4 :
                    val = int(input('enter your value to be converted '))
                    print('{} M is equal to {} in'.format(val, val*63360))
                elif way == 5:
                    print('changing category...')
                    break
                elif way == 6:
                    print('thankyou for using our calculator')
                    exit()
                
                else:
                    print('pls select a valid option')
        elif typ == 'currency':
            while True:
                way = int(input('Enter option no. (1: inr -> usd, 2: aed -> usd, 3: aed -> inr, 4: GBP -> inr, 5: GBP -> usd, 6: Change category, 7: Exit) '))
                
                if way == 1:
                    val = int(input('enter your value to be converted '))
                    print('{} rupees is equal to {} dollars'.format(val, val/74.9))
                elif way == 2:
                    val = int(input('enter your value to be converted '))
                    print('{} dhirams is equal to {} dollars'.format(val, val / 3.67))
                elif way == 3:
                    val = int(input('enter your value to be converted '))
                    print('{} dhirams is equal to {} rupees'.format(val, val *20.39))
                elif way == 4:
                    val = int(input('enter your value to be converted '))
                    print('{} GBP is equal to {} rupees'.format(val, val*98.16))
                elif way == 5:
                    val = int(input('enter your value to be converted '))
                    print('{} GDP is equal to {} dollars'.format(val, val * 1.31))
                elif way == 6:
                    print('changing category...')
                    break
                elif way == 7:
                    print('thankyou for using our calculator')
                    exit()
                else:
                    print('pls select a valid option')
        else:
            print('pls select a valid converion type')
                
            
        
    
        
        
            
            
                  
                      


