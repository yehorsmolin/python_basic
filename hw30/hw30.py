class UserException(Exception):

    def __init__(self, message="You can't add any more students to this group!"):
        self.message = message
        super().__init__(self.message)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, gender = {self.gender}, age = {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student {super().__str__()}, book record = {self.record_book}'


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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

st_list = [Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
            Student('Male', 32, 'Sam', 'Winchester', 'AN144'),
            Student('Male', 12, 'Clover', 'Field', 'AN146'),
            Student('Male', 16, 'Dave', 'Johnson', 'AN147'),
            Student('Male', 44, 'Vanya', 'Tarasov', 'AN148'),
            Student('Male', 22, 'Andrew', 'Tomson', 'AN149'),
            Student('Female', 17, 'Clara', 'Forrest', 'AN151'),
            Student('Female', 29, 'Rachel', 'Likes', 'AN152'),
            Student('Female', 45, 'Ann', 'Campbell', 'AN153')]

for st in st_list:
    gr.add_student(st)

print(gr)

st11 = Student('Male', 33, 'Mustafa', 'Velaskes', 'AN154')

gr.add_student(st11) # можна перевірити так

# try:
#    gr.add_student(st11)
# except UserException as err:  # або так
#    print(err)