import os
# 수강생 관리 시스템
todos = []

# 일정 등록
def register(todo):
    if is_exist(todo['todoNum']) < 0:
        todos.append(todo)
        return "{0}(이)가 등록되었습니다.".format(title)
    return "등록에 실패했습니다."

# 일정 목록
def getAllTodos():
    return todos

# 일정 삭제
def remove(todoNum):
    index = is_exist(todoNum)
    if index >= 0:
        todos.pop(index)
        return "{}가 삭제되었습니다.".format(todoNum)
    return "{}는 없는 아이디입니다.".format(todoNum)

# 일정 리스트 전체 삭제
def clear():
    todos.clear()
    return "일정이 모두 삭제되었습니다."

def menu_display():
    print("====== 일정 관리 시스템 ======")
    print("1. 할일 등록")
    print("2. 할일 목록 보기")
    print("3. 할일 삭제")
    print("4. 할일 리스트 전체 삭제")
    print("0. 종료")

def message_display(message):
    print(message)

def is_exist(todoNum):
    for index, todo in enumerate(todos):
        if todo["todoNum"] == todoNum:
            return index
    return -1

# 프로그램 종료시 list students "students.dat" 파일 저장
def save_list():
    save_file = open("todos.dat", "w")
    for index, todo in enumerate(todos):
        save_file.write("{}번째 | {}, {}\n".format(index, todo["todoNum"], todo['title']))

    save_file.close()
# 프로그램 시작시 "students.dat" 파일이 존재하고 정보가 있는 경우 list studetns 초기화
def init_data_load():
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                todo = data.split("|")[1].strip("\n").split(', ')
                todos.append({"todoNum":todo[0].strip(), "title":todo[1]})
            if not data: break
        read_file.close()

init_data_load()

while True:
    menu_display()
    menu = input("메뉴를 선택하세요 : ")
    
    if menu == "1":
        todoNum = input("아이디를 입력하세요 : ")
        title = input("일정을 입력하세요 : ")

        todo = {"todoNum":todoNum, "title":title}
        message_display(register(todo))
    elif menu == "2":
        print("====== 할일 목록 보기 ======")
        for t in todos:
            print("아이디:{0} 일정:{1}".format(t["todoNum"], t["title"]))
    elif menu == "3":
        for t in todos:
            print("아이디:{0} 일정:{1}".format(t["todoNum"], t["title"]))
        todoNum = input("삭제할 일정의 아이디 입력하세요 : ")
        message_display(remove(todoNum))

    elif menu == "4":
        message_display(clear())
    elif menu == "0":
        print("TODO 프로그램을 종료합니다.")
        save_list()
        break
    else:
        print("잘못 입력하셨습니다.")