import numpy as np
import re
class Soldier:
    def __init__ (self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.health = 100
    def display_info(self):
        print(f'health: {self.health}\nlocation: {self.x} {self.y}')
           
class Melee(Soldier):
    def __init__ (self,id, x, y):
       super().__init__(id, x, y)
       self.damage = 20

    
class Archer(Soldier):
    def __init__ (self,id, x, y):
       super().__init__(id, x, y)
       self.damage = 10


#Patterns:
create_soldier = r"^new\s(melee|archer)\s([0-9]|[1-4][0-9]|49)\s([0-9]|[1-9][0-9]|100)\s([0-9]|[1-9][0-9]|100)$"
move = r"^move\s([0-9]|[1-4][0-9]|49)\s(up|down|left|right)$"
attack = r"^attack\s([0-9]|[1-4][0-9]|49)\s([0-9]|[1-4][0-9]|49)$"
info = r"^info\s([0-9]|[1-4][0-9]|49)$"
status = r"who is in the lead?"
end = r"end"

def move_soldier(soldier, direction, n):
    if direction == 'down':
        if soldier.y < (n - 1):
            soldier.y += 1
        else:
            print('out of bounds')
            return False
    if direction == 'up':
        if soldier.y == 0:
            print('out of bounds')
            return False
        else:
            soldier.y -= 1
    if direction == 'right':
        if soldier.x < (n - 1):
            soldier.x += 1
        else:
            print('out of bounds')
            return False
    if direction == 'left':
        if soldier.x == 0:
            print('out of bounds')
            return False
        else:
            soldier.x -= 1
    return True

def Hdistance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


n = int(input())

soldiers = np.empty((2,50), dtype = object)
soldiers[:] = None
turn = 0

while(True):
    turn = turn % 2
    command = input()
    command_list = command.split()
    if re.match(end, command): 
        break
    elif re.match(create_soldier, command):
        if soldiers[turn][int(command_list[2])] != None:
            print('duplicate tag')
            continue
            
        if command_list[1] == 'melee':
            soldier = Melee(int(command_list[2]), int(command_list[3]), int(command_list[4]))
        else:
            soldier = Archer(int(command_list[2]), int(command_list[3]), int(command_list[4]))
            
        soldiers[turn][int(command_list[2])] = soldier

    elif re.match(move, command):
        soldier = soldiers[turn][int(command_list[1])]
        done = move_soldier(soldier, command_list[2], n )
        if not done:
            continue

    elif re.match(attack, command):
        attacker = soldiers[turn][int(command_list[1])]
        target = soldiers[(turn + 1) % 2][int(command_list[2])]
        distance = Hdistance(attacker.x, attacker.y, target.x, target.y)
        if isinstance(attacker, Melee):
            if distance <= 1:
                target.health -= attacker.damage
            else:
                print('the target is too far')
                continue
        else: # attacker is archer
            if distance <= 2:
                target.health -= attacker.damage
            else:
                print('the target is too far')
                continue
        if target.health <=0:
            soldiers[(turn + 1) % 2][int(command_list[2])] = None
            print('target eliminated')

    elif re.match(info, command):
        if soldiers[turn][int(command_list[1])] == None:
            print('soldier does not exist')
            continue       
        else:
            soldiers[turn][int(command_list[1])].display_info()
    elif re.match(status, command):
        player1, player2 = 0, 0
        for i in range(50):
            if soldiers[0][i] != None:
                player1 += soldiers[0][i].health
            if soldiers[1][i] != None:
                player2 += soldiers[1][i].health
        if player1 > player2:
            print('player 1')
        elif player2 > player1:
            print('player 2')
        else:
            print('draw')
        continue
    else:
        continue
    turn += 1
            
        
            
        
            
