class Course:
    def __init__(self, code, name, credits, is_elective, description):
        self.code = code                # str: unique ID, also the vertex in the graph
        self.name = name                # str: full course name
        self.credits = credits          # int: number of credits for the course
        self.is_elective = is_elective  # bool: True if the course is an elective, False if it is a core course
        self.description = description  # str: a brief description of the course

    def __str__(self):
        if self.is_elective:
            kind = "Elective"
        else:
            kind = "Required"
        return f"{self.code:<8} | {self.name:<32} | {kind}"

    def details(self):
        if self.is_elective:
            return (f"Code          : {self.code}\n"
                    f"Name          : {self.name}\n"
                    f"Credits       : {self.credits}\n"
                    f"Type          : Elective\n"
                    f"Description   : {self.description}")
        return (f"Code          : {self.code}\n"
                f"Name          : {self.name}\n"
                f"Credits       : {self.credits}\n"
                f"Type          : Required\n"
                f"Description   : {self.description}")