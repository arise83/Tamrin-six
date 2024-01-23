def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


functions = ['sum', 'average', 'lcd', 'gcd', 'max', 'min']
function = input()
if function not in functions :
    print('Invalid command')
else:
    list = []
    while True:
        a = input()
        if a != 'end' :
            if a.lstrip('-').isdigit():
                a = int(a)
                list.append(a)
            else :
                print('Invalid command')
        else :
            break
        
        
if function == 'sum' :
    print(sum(list))
    
elif function == 'average' :
     if len(list) > 0:
         a = sum(list) / len(list)
         a = float(a)
         print(round(a, 2))
   
elif function == 'lcd' : 
    m = max(list)
    counter =1
    while True:
        m = counter * max(list)
        sum = 0
        for value in list:
            sum+= (m % value)
        if sum == 0 :
            break
        else :

            counter += 1
    print(m)

       
elif function == 'gcd' :
         x =list[0]
         for i in range(1,len(list)):
             x = gcd(x,list[i])
         print(x)
                                
elif function == 'min' :
    print(min(list))
    
elif function == 'max' :
    print(max(list))
    
               