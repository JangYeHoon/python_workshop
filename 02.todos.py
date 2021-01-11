# 수강생 관리 시스템
todos = []
todoNum = 1

while True:
    print("====== Cloud MSA반 수강생 관리 시스템 ======")
    print("1. 할일 등록")
    print("2. 할일 목록 보기")
    print("3. 할일 삭제")
    print("4. 할일 리스트 전체 삭제")
    print("0. 종료")
    menu = input("메뉴를 선택하세요 : ")
    
    if menu == "1":
        title = input("일정을 입력하세요 : ")

        todos.append({"todoNum":todoNum, "title":title})
        print("{0}(이)가 등록되었습니다.".format(title))
        todoNum += 1
    elif menu == "2":
        print("====== 할일 목록 보기 ======")
        for t in todos:
            print("아이디:{0} 일정:{1}".format(t["todoNum"], t["title"]))
    elif menu == "3":
        for title in todos:
            print("아이디:{0} 일정:{1}".format(t["todoNum"], t["title"]))
        
        num = input("삭제할 일정의 아이디 입력하세요 : ")
        while not num.isdecimal():
            print("아이디는 숫자로 입력해주세요.")
            num = input("삭제할 일정의 아이디 입력하세요 : ")
        num = int(num) - 1

        del todos[num]
        print("{0}번이 삭제되었습니다.".format(num+1))
    elif menu == "4":
        todos.clear()
        print("일정이 모두 삭제되었습니다.")
    elif menu == "0":
        print("TODO 프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")