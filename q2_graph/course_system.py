from graph import Graph
from course import Course

graph = Graph()
courses = {}    # dictionary to hold course objects

predefined = [

    Course("MTH110", "Discrete Mathematics", 3, False, "Logic, sets, relations and proofs."),
    Course("PRG110", "Introduction to Programming", 4, False, "Variables, loops and functions in Python."),
    Course("PRG210", "Object-Oriented Programming", 4, False, "Classes, objects and inheritance."),
    Course("DBS230", "Database Systems", 3, False, "Tables, SQL queries and database design."),
    Course("ALG220", "Data Structures and Algorithms", 4, False, "Lists, trees, graphs, sorting and searching."),
    Course("AIN310", "Introduction to AI", 4, False, "Search, logic and basic machine learning."),
    Course("DSC320", "Fundamentals of Data Science", 3, True, "Cleaning, analysing and visualising data."),
    Course("WEB330", "Web Development", 3, True, "HTML, CSS and building web applications."),

]

for course in predefined:
    courses[course.code] = course
    graph.addVertex(course.code)

# the arrow goes FROM the prerequisite TO the course that requires it
prerequisites = [
 
    ("PRG110", "PRG210"),
    ("PRG110", "DBS230"),
    ("PRG210", "ALG220"),
    ("MTH110", "ALG220"),
    ("ALG220", "AIN310"),
    ("MTH110", "DSC320"),
    ("DBS230", "DSC320"),
    ("PRG210", "WEB330"),
    ("DBS230", "WEB330"),

]

for before, after in prerequisites:
    graph.addEdge(before, after)

def ask_course_code(message):
    # Ask for a course code and only return if that course exists. 
    # Otherwise, print an error message and return None.
    code = input(message).strip().upper()
    if code not in courses:
        print(f"Course code {code} not found.")
        return None
    return code

# Print each course in a list of codes, or a message if the list is empty.
def print_course_code(codes, empty_message):
    if len(codes) == 0:
        print(empty_message)

    for code in codes:
        print(courses[code])

while True:
    print("\n====== Course Prerequisite System ======")    
    print("1. List all courses")
    print("2. Show course details")
    print("3. Show prerequisites for a course")
    print("4. Show courses that require a course")
    print("5. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        for code in courses:
            print(courses[code])
    
    elif choice == "2":
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(courses[code].details())
    
    elif choice == "3":    
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(f"Prerequisites for {code}:")
            print_course_code(graph.listOutgoingAdjacentVertex(code), "None (no courses require this course)")

    elif choice == "4":
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(f"Courses that require {code}:")
            print_course_code(graph.listIncomingAdjacentVertex(code), "None (this course has no prerequisites)")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1-5.")