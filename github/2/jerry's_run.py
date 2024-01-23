n = int(input())
move = 0
list = []
for i in range(n):
    list.append('.')
List = []
List.extend([list.copy()])
i = 0
j = 0
List[0][0] = '*'
while move != 'END':
    move = input()
    if move == 'B':
        List.extend([list.copy()])
        j += 1
    elif move == 'R' and i != n-1:
        i += 1
    elif move == 'L' and i != 0:
        i -= 1
    List[j][i] = '*'
for t in range(len(List)):
    print(*List[t])
if i != n-1:
    print("There's no way out!")