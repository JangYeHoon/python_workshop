from controller.todo_controller import TodoController
from view.view import menu_display, menu_select, input_display, delete_display

controller = TodoController()
controller.file_read()

while True:
    menu_display()
    menu = menu_select()
    
    if menu == "1":
        todo = input_display()
        controller.register(todo)

    elif menu == "2":
        controller.getAllTodos()

    elif menu == "3":
        controller.getAllTodos()
        todoNum = delete_display()
        controller.remove(todoNum)

    elif menu == "4":
        controller.clear()

    elif menu == "0":
        print("TODO 프로그램을 종료합니다.")
        controller.file_write()
        break
    else:
        print("잘못 입력하셨습니다.")