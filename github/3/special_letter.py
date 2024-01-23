def find_pair(numbers, ans):
    temp_dict = {}
    result = {}
    for i, num in enumerate(numbers):
        temp_dict[int(num)] = i
    
    for val in temp_dict.keys():
        dif = ans - val
        if dif in temp_dict.keys() and dif != val :
            sum = temp_dict[val] + temp_dict[dif]
            if (val,dif) and (dif, val) not in result.keys():
                result[(val,dif)]= sum
    
    return result



n = input()
numbers = n.split()
ans = int(input())

result = find_pair(numbers, ans)
if result:
    for i in sorted(result.values()):
        print(i)
else:
    print('Not Found!')