import random

def create_outline():
    course_topics = {"* Introduction to Python", "* Tools of the Trade", "* How to make decisions", "* How to repeat code", "* How to structure data", "* Functions", "* Modules"}
    print("Course Topics:") # step 1
    list_topics = list(course_topics) # step 4(sorting list alphabetically))
    list_topics.sort()
    for x in (list_topics):
        print(x)
    print("Problems:") # Step 2
    for problems in (course_topics):
        print(problems + " : Problem 1, Problem 2, Problem 3")
    print("Student Progress:") # step 3
    for Tracking in range(0, 1):
        student_names = ("Siyamukelo", "Lesedi", "Kwena")
        problems = ("Problmes 1", "Problmes 2", "Problems 3")
        name_random = random.randint(0, len(student_names) - 1)
        name = student_names[name_random]
        problem_random = random.randint(0, len(problems) - 2)
        problem = problems[problem_random]
        course_list = list(course_topics)
        course_random = random.randint(0, len(course_list) - 2)
        Topic = course_list[course_random]
        Grades = ("[GRADED]", "[STARTED]", "[COMPLETED]")
        Grades_Random = random.randint(0, len(Grades) - 2)
        Status = Grades[Grades_Random]
        Tracking_progress = [name, Topic, problem, Status ]
        print(f"1.{name} - {Topic} - {problem} [STARTED]") # Step (sorting)
    for Tracking in range(0,1):
        student_names = ("Siyamukelo", "Lesedi", "Kwena", "Kang")
        problems = ("Problmes 1", "Problmes 2", "Problems 3", "Problmes 4")
        name_random = random.randint(0, len(student_names) - 1)
        name = student_names[name_random]
        problem_random = random.randint(0, len(problems) - 2)
        problem = problems[problem_random]
        course_list = list(course_topics)
        course_random = random.randint(0, len(course_list) - 2)
        Topic = course_list[course_random]
        Grades = ("[GRADED]", "[STARTED]", "[COMPLETED]")
        Grades_Random = random.randint(0, len(Grades) - 2)
        Status = Grades[Grades_Random]
        Tracking_progress = [name, Topic, problem, Status ]
        print(f"2.{name} - {Topic} - {problem} [GRADED]")
    for Tracking in range(0,1):
        student_names = ("Siyamukelo", "Lesedi", "Kwena", "Kang") # list of names stored in tuples
        problems = ("Problmes 1", "Problmes 2", "Problems 3", "Problmes 4") #a list of problems
        name_random = random.randint(0, len(student_names) - 1) # randomly indexes a name in Student_ ames
        name = student_names[name_random]                       #name is stored in variable name
        problem_random = random.randint(0, len(problems) - 2)#Randomly generatates index postion of a problem
        problem = problems[problem_random]                   #Problmem stored in variable, 
        course_list = list(course_topics)                    #coverting set to list
        course_random = random.randint(0, len(course_list) - 2) #randomly generate topic
        Topic = course_list[course_random]
        Grades = ("[GRADED]", "[STARTED]", "[COMPLETED]", "[RANGE]")
        Grades_Random = random.randint(0, len(Grades) - 2)
        Status = Grades[Grades_Random]
        Tracking_progress = [name, Topic, problem, Status ]
        print(f"3.{name} - {Topic} - {problem} [COMPLETED]")
      
        
        

 

    


    pass


if __name__ == "__main__":
    create_outline()
