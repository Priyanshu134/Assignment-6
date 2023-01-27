class Student:
    pass

class Marks:
    pass

Priyanshu=Student()

Priyanshu_ke_marks=Marks()

print("Priyanshu is an instance of class Student:",isinstance(Priyanshu,Student))
print("Priyanshu is an instance of class Marks:",isinstance(Priyanshu,Marks))
print("Priyanshu_ke_marks is an instance of class Student:",isinstance(Priyanshu_ke_marks,Student))
print("Priyanshu_ke_marks is an instance of class Marks:",isinstance(Priyanshu_ke_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))