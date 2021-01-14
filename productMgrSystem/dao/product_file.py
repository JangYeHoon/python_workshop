import os.path
from entity.product import Product

# 프로그램 종료시 list students "students.dat" 파일 저장
def file_write(products):
    save_file = open("products.dat", "w")
    for index, product in enumerate(products):
        save_file.write("{}번째 | {}, {}, {}, {}\n".format(index, product.p_id, product.p_name, product.price, product.description))

    save_file.close()

# 프로그램 시작시 "students.dat" 파일이 존재하고 정보가 있는 경우 list studetns 초기화
def file_read():
    products = []
    fileExist = os.path.isfile("products.dat")
    if fileExist:
        read_file = open("products.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                product = data.split("|")[1].strip("\n").split(', ')
                products.append(Product(product[0].strip(), product[1], int(product[2]), product[3]))
            if not data: break
        read_file.close()
    return products