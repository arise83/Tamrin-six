txt = str(input())
ans = txt.split(' ')
ans.sort(key=lambda x: int(x[1:]))
for i in ans :
    print(i[0],end='')