from entity.todo import Todo

def menu_display():
    print("====== 일정 관리 시스템 ======")
    print("1. 할일 등록")
    print("2. 할일 목록 보기")
    print("3. 할일 삭제")
    print("4. 할일 리스트 전체 삭제")
    print("0. 종료")

def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return menu

def message_display(message):
    print(message)

def list_display(todos):
    print("====== 할일 목록 보기 ======")
    for t in todos:
            print("아이디:{0} 일정:{1}".format(t.todoNum, t.title))

def input_display():
    todoNum = input("아이디를 입력하세요 : ")
    title = input("일정을 입력하세요 : ")

    return Todo(todoNum, title)

def delete_display():
    todoNum = input("삭제할 일정의 아이디 입력하세요 : ")
    return todoNum

