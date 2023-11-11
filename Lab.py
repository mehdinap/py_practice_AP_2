class Lab:
    student = []
    teacher = ""
    dayOfWeek = ""
    avgGrade = 0
    sizeOfClass = 0

    def __init__(self, thname, dayWeek) -> None:
        self.teacher = thname
        self.dayOfWeek = dayWeek

    def get_avg(self) -> int:
        sum = 0
        for i in self.student:
            sum += i.grade
            self.sizeOfClass += 1
        return sum / self.sizeOfClass

    def print_students(self) -> None:
        for i in self.student:
            print("\t", end="")
            print(i.firstname, i.lastname)

    def print_lab_info(self) -> None:
        print("teacher:", self.teacher, "\nday of week:", self.dayOfWeek,
              "\navg of grades:", self.get_avg(), "\nnumber of students:", self.sizeOfClass, "\nlist of students:")
        self.print_students()
