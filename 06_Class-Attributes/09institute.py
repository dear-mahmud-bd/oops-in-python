class Student:
    def __init__(self, name, semester, id) -> None:
        self.name = name
        self.id = id
        self.semester = semester
    def __repr__(self) -> str:
        return f'Student name: {self.name}, Semester: {self.semester}, Id: {self.id}'
# sifat = Student('Sifu', 4, 2102002)
# print(sifat)


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.subject}'
# sajibul = Teacher('Bujurgo', 'ICT', 1288)
# print(sajibul)


class Institute:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 1288
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    def admit(self, name, result, fee):
        if result<120:
            print(f"{name} you don't have enough result")
        elif fee<50500:
            print(f"{name} you don't have enough fees")
        else:
            id = len(self.students) + 2102001
            student = Student(name, 'L-1, T-1', id)
            self.students.append(student)
            print(f'{name} is enrolled with id: {id}, extra money {fee - 50500}')
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'

niter = Institute('NITER')
niter.admit('Ami TOPU', 164, 52000)
niter.admit('Saurav', 163, 50500)
niter.admit('Ros', 161, 70000)
niter.admit('Aurpi', 158, 90000)
niter.admit('Saikat', 155, 119000)
niter.admit('Momen', 154, 50500)
niter.admit('Sristy', 141, 9000)
niter.add_teacher('Anonna', 'Social Science')
niter.add_teacher('Ahsan', 'Data Structure')
niter.add_teacher('Aslam', 'App Development')
niter.add_teacher('Rakib', 'Abba Nehi Manega')
niter.add_teacher('Samiul', 'Algorithm')
niter.add_teacher('Sutrodhor', '071 vlo-basa diben')
niter.add_teacher('Sanzid', 'Bong Chong')
niter.add_teacher('Tanjim', 'Database')
print(niter)