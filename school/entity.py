class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info(self):
        print("아이디 : {} 이름 : {} ".format(self.id, self.name), end=",")

    def __str__(self):
        return "아이디 : {} 이름 : {} ".format(self.id, self.name)

    def __eq__(self, value):
        return self.id == value.id

class Student(Person):
    staticVariable = 0 # 클래스 변수: 객체생성하지 않고 클래스이름으로 참조
    def __init__(self, id, name, major):
        super().__init__(id, name)
        self.major = major
    
    def info(self):
        super().info()
        print("전공 : {}".format(self.major))
    
    def __str__(self):
        return super().__str__() + " 전공 : {}".format(self.major)
    
    def __eq__(self, value):
        return super().__eq__(value)
    
    classmethod
    def classMethod(self, parameter_list):  # 클래스이름.메서드 : Student.classMethod()
        pass

class Teacher(Person):
    def __init__(self, id, name, subject):
        super().__init__(id, name)
        self.subject = subject

    def info(self):
        super().info()
        print("과목 : {}".format(self.subject))

    def __str__(self):
        return super().__str__() + " 과목 : {}".format(self.subject)

class Employee(Person):
    def __init__(self, id, name, department):
        super().__init__(id, name)
        self.department = department
    
    def info(self):
        super().info()
        print("부서 : {}".format(self.department))

    def __str__(self):
        return super().__str__() + " 부서 : {}".format(self.department)

student = Student("CMSA07", "박기윤", "정보통신")
student2 = Student("CMSA07", "박기윤", "정보통신")
teacher = Teacher("T01", "박성민", "함수형프로그램")
employee = Employee("E001", "심아윤", "연구소")

# __eq__ 재정의하기 전 객체의 주소값 비교 : student != student2
# __eq__ 재정의한 후 (id값 비교) : student == student2
if student == student2:
    print("student == student2")
else:
    print("student != student2")

print("instance student Student : ", isinstance(student, Student))
print("instance student Teacher : ", isinstance(student, Teacher))
print("instance student Person : ", isinstance(student, Person))

# student.student_info()
# teacher.teacher_info()
# employee.employee_info()
# 다형성 : 한 가지 타입으로 여러형태 사용
#           Super에서 제공되는 method를 Sub에서 재정의할 수 있다. 사용자가 Super의 method와 같은 이름의 method 생성
#           호출하더라도 재정의된 Sub의 method가 다양하게 응답할 수 있다.
student.info()
teacher.info()
employee.info()

# print(student)
# print(teacher)
# print(employee)