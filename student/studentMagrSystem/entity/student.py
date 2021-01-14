class Student:
    # 생성자 : id, name, age, major
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major
    
    # 객체의 id가 같은 경우 True
    def __eq__(self, id):
        return self.id == id
    
    def __str__(self):
        return "학번 : {} 이름 : {} 나이 : {} 전공 : {}".format(self.id, self.name, self.age, self.major)