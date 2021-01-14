from controller.product_controller import ProductController
from view.view import menu_display, menu_select, input_display, update_display, remove_display

controller = ProductController()

controller.file_read()

while True:
    menu_display()
    menu = menu_select()

    if menu == 1:
        product = input_display()
        controller.register(product)
        
    elif menu == 2:
        controller.getAllProduct()

    elif menu == 3:
        controller.getAllProduct()
        p_id, description = update_display()
        controller.update(p_id, description)
    
    elif menu == 4:
        controller.getAllProduct()
        p_id = remove_display()
        controller.remove(p_id)
    
    elif menu == 0:
        print("프로덕트 관리 시스템을 종료합니다.")
        controller.file_write()
        break

    else:
        print("없는 메뉴입니다.")