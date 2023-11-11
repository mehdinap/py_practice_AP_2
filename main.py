from Student import Student
from Lab import Lab

if __name__ == "__main__":
    std1 = Student("mehdi", "najibpour", "40131054")
    std2 = Student("ali", "mojodi", "40126093")

    std1.set_grade( 18)
    std2.set_grade( 17.5)

    std1.print_info()
    std2.print_info()


