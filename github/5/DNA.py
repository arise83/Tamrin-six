import re

class Crab:
    def __init__ (self, dna):
        self.build_dna(dna)

    def build_dna(self, dna):
        dna_end = dna[0:10]
        self.dna = dna + dna_end
        
    def display(self):
        self.dna = self.dna.replace("tt", "o")
        print(self.dna)

class Bob(Crab):
    def __init__ (self, dna):
        super().__init__(dna)

    def display(self):
        list_of_length = list(map(int, str(len(self.dna))))
        list_of_length = self.merge_sort(list_of_length)
        print(self.list_to_num (list_of_length))

    def merge_sort(self, list):
        if len(list) <= 1:
            return list

        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)

        return self.merge(left_list, right_list)

    def merge(self, left_list, right_list):
        sorted_list = []
        left_index = 0
        right_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        sorted_list += left_list[left_index:]
        sorted_list += right_list[right_index:]

        return sorted_list

    def list_to_num (self,lst):
        num = 0
        for digit in lst:
            num = num * 10 + digit 
        return num

class Octopus:
    def __init__ (self, dna):
        self.build_dna(dna)

    def build_dna(self, dna):
        idx = self.linear_search(dna)
        if idx != -1:
            self.dna = dna + str(idx)
        else:
            self.dna = dna
        
    def linear_search(self, dna):
        for i in range(len(dna)):
            if dna[i] == 'x':
                return i
        return -1    

    def display(self):
        pattern = r'(\w)\1{2}'
        print(re.sub(pattern, '(0_0)', self.dna))

def reverse(string):
    return string[::-1]
        

input_string = input()
if len(input_string) < 10 or len(input_string)>1000:
    print('invalid input')
elif input_string[0] == 'm':
    crab = Crab(input_string)
    crab.display()
elif input_string[0] == 's' and input_string[1] == 'b' :
    bob = Bob(input_string)
    bob.display()
elif input_string[0] == 's' and input_string[1] != 'b' :
    octopus = Octopus(input_string)
    octopus.display()
elif input_string[-1] == 'm': 
    crab = Crab(reverse(input_string))
    crab.display()

elif input_string[-1] == 's' and input_string[-2] == 'b' :
    bob = Bob(reverse(input_string))
    bob.display()

elif input_string[-1] == 's' and input_string[-2] != 'b' :
    octopus = Octopus(reverse(input_string))
    octopus.display()
else:
    print('invalid input')
    
