import re
class User:
    def __init__  (self, type, id, name, password):
        self.type = type
        self.id = id
        self.name = name
        self.password = password


class Course:
    def __init__ (self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.total_students = 0

def display_courses(courses):
    print('course list:')
    for key, value in courses.items():
        print(f'{key} {value.name} {value.total_students}/{value.capacity}')
    

#----- Professor menu -------
 
def professor_menu(courses, course_students):
    #Patterns
    add_course_pattern = r"^edu add course -c \S+ -i \d+ -n \d+ edu$"
    end_pattern = r"^edu exit edu$"
    display_courses_pattern = r"^edu show course list edu$"
    log_out_pattern = r"^edu log out edu$"
    add_course_selection = r"^edu add course -c .*edu$"

    print('logged in successfully!\nentered professor menu')
    
    repeat = True
    while(repeat):
        command =input().strip()
        if re.match(end_pattern, command):
            return False
        elif re.match(display_courses_pattern, command):
            display_courses(courses)
        elif re.match(log_out_pattern, command):
            print('logged out successfully!\nentered log in/sign up menu')
            return True
        elif re.match(current_state_pattern, command):
            print('professor menu')
        elif re.match(add_course_selection, command):
            if re.match(add_course_pattern, command):
                command_list = command.split()
                course_id = command_list[6]
                if course_id in courses.keys():
                    print('course id already exists')
                    continue
                else:
                    course = Course(course_id, command_list[4], command_list[8])
                    courses[course_id] = course
                    students_list = []
                    course_students[course_id] = students_list
                    print('course added successfully!')

            elif not re.search(r"-c [a-zA-Z]+ -i", command):
                print("invalid course name")
            elif not re.search(r"-i [0-9]+ -n", command):
                print("invalid course id")
            elif not re.search(r"-n [0-9]+ edu", command):
                print("invalid course capacity")
            else:
                print('invalid command')
        else:
            print('invalid command')
        
#----- Student menu -------           
            
def student_menu(courses, course_students, user_id):
    #Patterns  
    get_course_pattern = r"^edu get course -i \w+ edu$"
    end_pattern = r"^edu exit edu$"
    display_courses_pattern = r"^edu show course list edu$"
    log_out_pattern = r"^edu log out edu$"
    current_state_pattern = r"^edu current menu edu$" 

    print('logged in successfully!\nentered student menu')
    
    repeat = True
    while(repeat):
        command =input().strip()
        if re.match(end_pattern, command):
            return False
        elif re.match(display_courses_pattern, command):
            display_courses(courses)
        elif re.match(log_out_pattern, command):
            print('logged out successfully!\nentered log in/sign up menu')
            return True
        elif re.match(current_state_pattern, command):
            print('student menu')
        
        elif re.match(get_course_pattern, command):
            command_list = command.split()
            course_id = command_list[4]
            if course_id not in courses.keys():
               print('incorrect course id')
            else:
                course = courses.get(course_id)
                if course_id in course_students.keys():
                    students_list = course_students.get(course_id)
                    if students_list != None:
                        if user_id in students_list:
                            print('you already have this course')
                        elif int(course.total_students) == int(course.capacity):
                            print('course is full')
                        else:
                            students_list.append(user_id)
                            courses[course_id].total_students +=1
                            print('course added successfully!')                 
        
        else:
            print('invalid command')
            

       
users = {}
courses = {}
course_students = {}

#----- Log in menu -------
# Patterns:
sign_up_pattern = r"^edu sign up -[SP] -i \d+ -n \S+ -p (?=.*[()&^%$@!.*)])(?!\s)(.{4,}) edu$"
log_in_pattern = r"^edu log in -i \d+ -p (?=.*[()&^%$@!.*)])(?!\s)(.{4,}) edu$"
current_state_pattern = r"^edu current menu edu$"
end_pattern = r"^edu exit edu$"
log_in_selection = r"^edu log in .* edu$"
sign_up_selection = r"^edu sign up .* edu$"
password_pattern = r"-p (?=.*[()&^%$@!.*)])(?!\s)(.{4,}) edu"
log_out_pattern = r"^edu log out edu$"
display_courses_pattern = r"^edu show course list edu$"

repeat = True
while(repeat):
    command = input().strip()
    command_without_space = re.sub(' +', ' ', command)
    if command_without_space != command or re.match(log_out_pattern, command) or re.match(display_courses_pattern, command):
        print('invalid command')
        continue
    if re.match(end_pattern, command):
        repeat = False

    elif re.match(current_state_pattern, command):
        print('log in/sign up menu')
        
    elif re.match(log_in_selection, command):
        if re.match(log_in_pattern, command):
            command_list = command.split()
            id = command_list[4]
            if id in users:
                user = users[id]
                if user.password == command_list[6]:
                    if user.type == 'S':
                        result = student_menu(courses, course_students, id)
                        if not result:
                            repeat = False
                    else:
                        result = professor_menu(courses, course_students)
                        if not result:
                            repeat = False
                else:
                    print('incorrect password')
            else:
                print('incorrect id')
        elif not re.search(r"-i", command):
            print('invalid command')
        elif not re.search(r"-p", command):
            print('invalid command')
                
        elif not re.search(r"-i [0-9]+ -p", command):
            print("incorrect id")
        
        elif not re.search(password_pattern, command):
            print('incorrect password')
            
        else:
            print('invalid command')
            
    elif re.match(sign_up_pattern, command):
        
        command_list = command.split()
        id = command_list[5]
        if id in users:
            print("id already exists")
        else:
            type = command_list[3][1]
            user = User(type,id,command_list[7],command_list[9])   
            users[id] = user 
            print("signed up successfully!")
            
    elif not re.search(r"^edu sign up -[SP]", command):
        print("invalid type")
    elif not re.search(r"-i [0-9]+ -n", command):
        print("invalid id")
    elif not re.search(r"-n [a-zA-Z]+ -p", command):
        print("invalid name")
    elif not re.search(password_pattern, command):
        print("invalid password")
    else:
        print('invalid command')

                  
            















    
