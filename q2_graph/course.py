class Course:
    def __init__(self, code, name, credits, is_elective, description):
        self.code = code
        self.name = name
        self.credits = credits
        self.is_elective = is_elective
        self.description = description

    def __str__(self):
        if self.is_elective:
            kind = "Elective"
        else:
            kind = "Required"
        return f"{self.code:<8} | {self.name:<32} | {kind}"

    def details(self):
        if self.is_elective:
            return f"{self.code} - {self.name}\nThis is an elective course. Details are hidden."
        return (f"Code: {self.code}\n"
                f"Name: {self.name}\n"
                f"Credits: {self.credits}\n"
                f"Type: Core\n"
                f"Description: {self.description}")