def sumfac(number):
    sum = number
    f = 1
    while f < number :
        if number % f == 0 :
            sum += f
        f += 1
    return sum


def convert(a, b) :
    converted = 0
    pos = 0
    while a != 0 :
        r = a % b
        converted = converted + r * 10 ** pos
        a = a // b
        pos += 1
    return converted

sum = 0
invalid = False
while True :                
    a , b  = input().split( )
    a = int(a)
    b = int (b)
    if a == -1 and b == -1 :
        break
    if  b < 2 or b > 9 :
        invalid = True 
    else:
        sum += convert(sumfac(a), b) 
        
if invalid:
        print('invalid base!')
else:
        print(sum)
        
  

        

    