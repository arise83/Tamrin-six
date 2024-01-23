p_1 = int(input())
p_2 = int(input())
n = int(input())
list = []

while n:
    i = int(input())
    if i < 32:
        if p_1 & (1 << i):
            list.append("yes")
        else:
            list.append("no")
    else:
        if p_2 & (1 << (i-32)):
            list.append("yes")
        else:
            list.append("no")
    n-=1

for item in list:
    print(item)
                        
