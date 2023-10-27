from school import School, ClassRoom, Subject
from persons import Student, Teacher


def main():
    school = School("MGHS", "22,Sahid-rariq Saroni")

    class_eight = ClassRoom('eight')
    class_nine = ClassRoom('nine')
    class_ten = ClassRoom('ten')

    school.add_classroom(class_eight)
    school.add_classroom(class_nine)
    school.add_classroom(class_ten)

    abul = Student('Abul Khayer', class_ten)
    bablu = Student('Bablu Mia', class_ten)
    jorina = Student('Jorina Begum', class_nine)
    
    school.student_admission(abul)
    school.student_admission(bablu)
    school.student_admission(jorina)


    # Add teacher...
    physics_teacher = Teacher('Shahjahan Tapon')
    chemistry_teacher = Teacher('Haradon Nag')
    biology_teacher = Teacher('Azmal Sir')
    
    physics = Subject('physics', physics_teacher)
    chemistry = Subject('chemistry', chemistry_teacher)
    biology = Subject('biology', biology_teacher)
    
    class_ten.add_subject(physics)
    class_ten.add_subject(chemistry)
    class_ten.add_subject(biology)

    class_ten.take_semester_final()


    print(school)


# calling the main method...
if __name__ == "__main__":
    main()