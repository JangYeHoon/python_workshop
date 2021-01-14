from controller_view.student_controller import StudentController
from view_template.template_view import menu_display, menu_select, input_display, update_display, delete_display, message_display

controller = StudentController()

controller.file_read()

while True:
    menu_display()
    menu = menu_select()
    
    if menu == "1":
        student = input_display()
        controller.register(student)

    elif menu == "2":
        controller.getAllStudents()
        
    elif menu == "3":
        controller.getAllStudents()
        id, major = update_display()
        
        controller.update(id, major)
    elif menu == "4":
        controller.getAllStudents()
        id = delete_display()

        controller.remove(id)

    elif menu == "0":
        message_display("수강생 관리 프로그램을 종료합니다.")
        controller.file_write()
        break
    else:
        print()
        message_display("잘못 입력하셨습니다.")