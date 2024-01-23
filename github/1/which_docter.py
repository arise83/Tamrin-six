a = int(input())
b = int(input())
count = 0
x = a ^ b
while x != 0 :
    if (x & 1) == 1:
        count += 1
    x >>= 1
    
print(count)