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


LINE = "-" * 56

# Print each course in a list of codes, or a message if the list is empty.
def print_course_code(codes, empty_message):
    if len(codes) == 0:
        print(empty_message)
        return
    print(f"{'Code':<8} | {'Course Name':<32} | Type")
    print(LINE)
    for code in codes:
        print(courses[code])

while True:
    print()
    print("=" * 56)
    print("              COURSE PREREQUISITE SYSTEM")
    print("=" * 56)
    print("  1. List all courses")
    print("  2. Show course details")
    print("  3. Show prerequisites of a course")
    print("  4. Show courses unlocked by a course")
    print("  5. Add a new course")
    print("  6. Add a prerequisite")
    print("  7. Remove a prerequisite")
    print("  8. Exit")
    print(LINE)
    choice = input("Enter your choice (1-8): ").strip()
    print()


    if choice == "1":
        print(f"All courses ({len(courses)}):")
        print_course_code(list(courses), "No courses yet.")
    
    elif choice == "2":
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(LINE)
            print(courses[code].details())
            print(LINE)
    
    elif choice == "3":    
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(f"Prerequisites for {code} ({courses[code].name}):")
            print_course_code(graph.listIncomingAdjacentVertex(code), "None - this is an entry-level course.")

    elif choice == "4":
        code = ask_course_code("Enter course code: ")
        if code is not None:
            print(f"Courses that require {code} ({courses[code].name}):")
            print_course_code(graph.listOutgoingAdjacentVertex(code), "None - no course requires this one yet.")

    elif choice == "5":
        code = input("Enter new course code: ").strip().upper()
        
        if code == "":
            print("Course code cannot be empty.")
            continue
        if code in courses:
            print(f"Course code {code} already exists.")
            continue

        name = input("Enter course name: ").strip()
        if name == "":
            print("Course name cannot be empty.")
            continue
        try:
            credits = int(input("Credits: "))
        except ValueError:
            print("Credits must be a whole number.")
            continue
        if credits <= 0:
            print("Credits must be more than 0.")
            continue
        elective = input("Is it an elective? (y/n): ").strip().lower()
        if elective != "y" and elective != "n":
            print("Please enter y or n.")
            continue
        description = input("Description: ").strip()

        courses[code] = Course(code, name, credits, elective == "y", description)
        graph.addVertex(code)
        print(f"\n{code} ({name}) has been added.")

    elif choice == "6":
        before = ask_course_code("Prerequisite course code: ")
        
        if before is None:
            continue
        
        after = ask_course_code("Course that requires it: ")
        
        if after is None:
            continue
        if before == after:
            print("A course cannot be its own prerequisite.")
            continue
        if graph.hasPath(after, before):
            print(f"Cannot add: {after} already leads to {before}, so this would create a cycle.")
            continue
        if before in graph.listIncomingAdjacentVertex(after):
            print(f"{before} is already a prerequisite of {after}.")
            continue
        
        graph.addEdge(before, after)
        print(f"\n{before} is now a prerequisite of {after}.")

    elif choice == "7":
        before = ask_course_code("Prerequisite course code: ")
        
        if before is None:
            continue
        
        after = ask_course_code("Course that requires it: ")
        
        if after is None:
            continue
        if graph.removeEdge(before, after):
            print(f"\n{before} is no longer a prerequisite of {after}.")
        else:
            print(f"{before} is not a prerequisite of {after}.")

    elif choice == "8":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1-8.")