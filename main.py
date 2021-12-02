import pprint


class Student:
    school = "Per Scholas"

    def __init__(self, s_id , s_name, s_address):
        self.s_id = s_id
        self.s_name = s_name
        self.s_address = s_address

    @classmethod
    def from_fullname(cls, fullname):
        s_name = fullname
        return cls(200, fullname, "Plano")

    def all_info(self):
        return "{} {} {} {}".format(self.s_id, self.s_name, self.s_address, self.school )

    @staticmethod
    def print_hello():
        print("hello world")


student_chris = Student(100, "chris", "Philly")
student_jafer = Student(100, "jafer", "Dallas")
print(student_chris.s_id, student_chris.s_name, student_chris.s_address)
student_chris.email = "yang@gmail.com"
print(student_chris.email)
print(hasattr(student_chris, "email"))
print(hasattr(student_jafer, "s_id"))
pprint.pprint(vars(Student))
print(student_chris.all_info())

Student(100, "chris", "Philly")
student_example = Student.from_fullname("chris yang")
print(student_example)

Student.print_hello()


print(dir(student_chris))
