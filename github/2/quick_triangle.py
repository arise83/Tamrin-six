def fact(n):
    pro = 1
    for i in range(1, n+1):
        pro *= i
    return pro
        
def comb(n, k):
    t = fact(n) // (fact(n-k) * fact(k))
    return t

n = int(input())
if n == 1:
    print(1)
else :
    b = 1
    print('1\n')
    while b != n :
        k = 0
        while k != b +1:
            y = comb(b, k)
            print(y, end=' ')
            k += 1
        print('\n')
        b += 1