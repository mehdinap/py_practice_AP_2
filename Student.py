class Student:
    firstname = ""
    lastname = ""
    id = ""
    grade = 0

    def __init__(self, firstname, lastname, id) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def set_grade(self, grade) -> None:
        self.grade = grade

    def print_info(self) -> None:
        print(
            self.firstname,
            self.lastname,
            "\nID:", self.id,
            "\nGRADE:", self.grade,
            "\n"
        )
