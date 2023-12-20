from class_error import UserException

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.search = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise UserException
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '