import re
class Patient:
    def __init__(self, id, name, family, age, height, weight):
        self.id = id
        self.name = name
        self.family = family
        self.age = age
        self.height = height
        self.weight = weight
        
    def display(self):
        print("patient name: " + self.name)
        print("patient family name: " + self.family)
        print("patient age: " + self.age)
        print("patient height: " + self.height)
        print("patient weight: " + self.weight)
        
    def get_name(self):
        return self.name

    def get_family(self):
        return self.family

def add_patient(command_list):
    if command_list[2] in patients:
       print("error: this ID already exists")
    elif int(command_list[5]) < 0:
       print('error: invalid age')
    elif int(command_list[6]) < 0:
       print('error: invalid height')
    elif int(command_list[7]) < 0:
       print('error: invalid weight')
    else:
        patient = Patient(int(command_list[2]), command_list[3], command_list[4], command_list[5], command_list[6], command_list[7])
        patients[command_list[2]] = patient
        print("patient added successfully")

def display_patient(id):
    if id not in patients:
        print('error: invalid ID')
    else:
        patients[id].display()
        

def add_visit(id, beginning_time):
        if id not in patients:
            print("error: invalid id")
        elif int(beginning_time) < 9 or int(beginning_time) > 18 :
            print ("error: invalid time")
        elif beginning_time in visits:
            print ("error: busy time")
        else:
            visits[beginning_time] = id
            print ("visit added successfully!")

def delete_patient(id):
        delete_keys = []
        if id not in patients:
            print ("error: invalid id")
        else:
            del patients[id]
            for key, value in visits.items():
                if value == id:
                    delete_keys.append(key)
            for key in delete_keys:
                del visits[key]
            print ("patient deleted successfully!")

def display_visits():
    print ('SCHEDULE:')
    for key, value in visits.items():
        time = key
        print (time + ":00 " + patients[value].get_name() + " " + patients[value].get_family())
    

def get_command():
    #Patterns
    add_patient_command = r"^add patient (0|[1-9]\d*) ([a-zA-Z]+) ([a-zA-Z]+) -?(0|[1-9]\d*) -?(0|[1-9]\d*) -?(0|[1-9]\d*)$"
    display_patient_command = r"^display patient (0|[1-9]\d*)$"
    add_visit_command = r"^add visit (0|[1-9]\d*) (0|[1-9]\d*)$"
    delete_patient_command = r"^delete patient (0|[1-9]\d*)$"
    display_visit_list_command = r"^display visit list$"
 
    while True:
        input_command = input()
        input_command = input_command.strip()
        input_command = re.sub(' +', ' ', input_command)
        command_list = input_command.split()
     
        if re.match(add_patient_command, input_command): 
            add_patient(command_list)
        elif re.match(display_patient_command, input_command):
            display_patient(command_list[2])
        elif re.match(add_visit_command, input_command):
            add_visit(command_list[2], command_list[3])
        elif re.match(delete_patient_command, input_command):
            delete_patient(command_list[2])
        elif re.match(display_visit_list_command, input_command):
            display_visits()
        elif input_command == 'exit':
            break
        else:
            print('invalid command')

patients = {}
visits = {}
get_command()

