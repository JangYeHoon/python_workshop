# 수강생 관리 시스템
students = []

# 수강생 등록 : list students에 id중복체크하고 존재하지 않는 경우 정보 저장하고 message 리턴
def register(student):
    if (is_exist(student["id"]) < 0):
        students.append(student)
        return "{0}(이)가 등록되었습니다.".format(student['name'])
    return "이미 동록된 정보입니다."

# 수강생 목록 : list students 목록 리턴
def getAllStudents():
    return students

# 수강생 수정 : id를 검색해서 정보 수정하고 message 리턴
def update(id, key, change_value):
    print(id)
    index = is_exist(id)
    print(index)
    if index >= 0:
        students[index][key] = change_value
        return "{0}의 {1}이 수정되었습니다.".format(id, key)
    else:
        return "{0}의 정보가 존재하지 않습니다.".format(id)

# 수강생 삭제 : id를 검색해서 수강생 정보 삭제 message 리턴
def remove(student):
    index = is_exist(id)
    if index >= 0:
        students.pop(index)
        return "{0}번의 정보가 삭제되었습니다.".format(id)
    else:
        return "{0}의 정보가 존재하지 않습니다.".format(id)

# 수강생 존재여부 : id검색해서 list students의 index 값 리턴
def is_exist(id):
    for index, student in enumerate(students):
        if student["id"] == id:
            return index
    return -1

# menu display
def menu_display():
    print("====== Cloud MSA반 수강생 관리 시스템 ======")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")

# message display
def message_display(message=""):
    print(message)

while True:
    menu_display()
    menu = input("메뉴를 선택하세요 : ")
    
    if menu == "1":
        id = input("아이디를 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        age = input("나이를 입력하세요 : ")
        while not age.isdecimal():
            print("나이는 숫자로 입력해주세요.")
            age = input("나이를 입력하세요 : ")
        major = input("전공을 입력하세요 : ")

        student = {"id":id, "name":name, "age":int(age), "major":major}
        message_display(register(student))
    elif menu == "2":
        print("====== 수강생 목록 보기 ======")
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["id"], s["name"], s["age"], s["major"]))
    elif menu == "3":
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["id"], s["name"], s["age"], s["major"]))
        id = input("수정할 학생의 아이디 입력하세요 : ")

        key = input("수정할 키를 입력하세요(name, age, major) : ")
        change_value = input("수정할 값을 입력하세요 : ")
        
        message_display(update(id, key, change_value))
    elif menu == "4":
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["id"], s["name"], s["age"], s["major"]))
        id = input("삭제할 학생의 아이디 입력하세요 : ")

        message_display(remove(id))
    elif menu == "0":
        message_display("수강생 관리 프로그램을 종료합니다.")
        break
    else:
        print()
        message_display("잘못 입력하셨습니다.")