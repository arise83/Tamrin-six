o = int(input())
b  = int(input())
sum_of_o_b = int(input())
while o:
    x = (o & b) << 1
    y = o ^ b
    o = x
    b = y
print(b)
if b != sum_of_o_b :
    print("NO")
else:
    print("YES")