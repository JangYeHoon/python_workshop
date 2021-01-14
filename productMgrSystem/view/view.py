from entity.product import Product

# menu display
def menu_display():
    print("====== 프로덕트 관리 시스템 ======")
    print("1. 상품 정보 등록")
    print("2. 상품 목록 보기")
    print("3. 상품 정보 수정")
    print("4. 상품 정보 삭제")
    print("0. 종료")

# menu select display
def menu_select():
    menu = int(input("메뉴를 선택하세요 : "))
    return menu

# message display
def message_display(message=""):
    print(message)

# list display
def list_display(products):
    print("====== 수강생 목록 ======")
    for product in products:
        print("아이디:{0} 이름:{1} 가격:{2} 설명:{3}".format(product.p_id, product.p_name, product.price, product.description))
    
# Product input display
def input_display():
    p_id = input("아이디 : ")
    p_name = input("이름 : ")
    price = input("가격 : ")
    while not price.isdecimal():
            print("가격은 숫자로 입력해주세요.")
            price = input("가격 : ")
    description = input("설명 : ")

    return Product(p_id, p_name, int(price), description)

# Product update
def update_display():
    p_id = input("수정할 상품의 아이디 : ")

    description = input("설명 : ")
    return (p_id, description)

# Product remove
def remove_display():
    p_id = input("삭제할 상품의 아이디 : ")
    return p_id