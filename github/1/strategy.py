a, b = input().split()
a = int(a)
b = int(b)
if (a >= 0 and a <= 1000) and (b >= 0 and b <= 1000):
    number = 0
    if a <= b:
        if a <= 2 and b >= 2 :
            number += 1
        for num in range(a, b+1):
            prime = False
            for i in range(2, num):
                prime = True
                if (num % i) == 0:
                    prime = False
                    break
            if prime == True:
                number += 1
        print(f'main order - amount: {number}')
    else: 
        if b <= 2 and a >= 2 :
                number += 1
        for num in range(b, a+1):
            prime = False
            for i in range(2, num):
                prime = True
                if (num % i) == 0:
                    prime = False
                    break
            if prime == True:
                number += 1
        print(f'reverse order - amount: {number}')