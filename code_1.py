#The teacher was missing and the students prepare the class
#The oldest student will be the teacher and the youngest the assistant

#Ask for the name and age of the students who attended class

#Function to obtain the teacher and the assistant according to age
def information_students(num_students):
    students = []

    #For to request information from students
    for i in range(num_students):
        name = input("Enter student name: ")
        age = int(input("Enter the student's age: "))
        student = (name,age)
        #Adding information to the list
        students.append(student)
        
    #Sort by age
    students.sort(key=lambda x:x[1])
    
    #students[x] returns a tuple with [name, age] and then we access the name
    #to define the teacher and assistant
    assistant = students[0][0]
    teacher = students[-1][0]
    return assistant, teacher
        
       
#The number of students present in the class is obtained
number_students = int(input("How many students attended the class?: "))

#The values ​​returned by the function are unpacked into the assistant and teacher variables
assistant, teacher = information_students(number_students)

#The name of who will be the teacher and assistant is printed
print(f"El profesor es: {teacher} y su asistente es: {assistant}")