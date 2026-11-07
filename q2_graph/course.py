class Course:
    def __init__(self, code, name, credits, is_elective, description):
        self.code = code                # str: unique ID, also the vertex in the graph
        self.name = name                # str: full course name
        self.credits = credits          # int: number of credits for the course
        self.is_elective = is_elective  # bool: True if the course is an elective, False if it is a core course
        self.description = description  # str: a brief description of the course

    def course_type(self):
        # Turns the True/False flag into a word for display
        if self.is_elective:
            return "Elective"
        return "Required"

    def __str__(self):
        # One row of the course table
        return f"{self.code:<8} | {self.name:<32} | {self.course_type()}"

    def details(self):
        # Mandatory feature (b): shows ALL information, whether elective or not
        return (f"Code          : {self.code}\n"
                f"Name          : {self.name}\n"
                f"Credits       : {self.credits}\n"
                f"Type          : {self.course_type()}\n"
                f"Description   : {self.description}")

