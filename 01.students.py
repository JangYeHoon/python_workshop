# 수강생 관리 시스템
students = []
student_id = 1

while True:
    print("====== Cloud MSA반 수강생 관리 시스템 ======")
    print("1. 수강생 정보 등록")
    print("2. 수강생 목록 보기")
    print("3. 수강생 정보 수정")
    print("4. 수강생 정보 삭제")
    print("0. 종료")
    menu = input("메뉴를 선택하세요 : ")
    
    if menu == "1":
        name = input("이름을 입력하세요 : ")
        age = input("나이를 입력하세요 : ")
        while not age.isdecimal():
            print("나이는 숫자로 입력해주세요.")
            age = input("나이를 입력하세요 : ")
        major = input("전공을 입력하세요 : ")

        students.append({"student_id":student_id, "name":name, "age":int(age), "major":major})
        print("{0}(이)가 등록되었습니다.".format(name))
        student_id += 1
    elif menu == "2":
        print("====== 수강생 목록 보기 ======")
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["student_id"], s["name"], s["age"], s["major"]))
    elif menu == "3":
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["student_id"], s["name"], s["age"], s["major"]))
        num = input("수정할 학생의 아이디 입력하세요 : ")
        while not num.isdecimal():
            print("아이디는 숫자로 입력해주세요.")
            num = input("수정할 학생의 아이디 입력하세요 : ")
        num = int(num) - 1

        key = input("수정할 키를 입력하세요(name, age, major) : ")
        while students[num].get(key) == None:
            key = input("student 속성 입력(name, age, major) : ")
        change_value = input("수정할 값을 입력하세요 : ")
        students[num][key] = change_value
        print("{0}의 {1}이 수정되었습니다.".format(num+1, key))
    elif menu == "4":
        for s in students:
            print("아이디:{0} 이름:{1} 나이:{2} 전공:{3}".format(s["student_id"], s["name"], s["age"], s["major"]))
        num = input("삭제할 학생의 아이디 입력하세요 : ")
        while not num.isdecimal():
            print("아이디는 숫자로 입력해주세요.")
            num = input("삭제할 학생의 아이디 입력하세요 : ")
        num = int(num) - 1

        del students[num]
        print("{0}번이 삭제되었습니다.".format(num+1))
    elif menu == "0":
        print("수강생 관리 프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")