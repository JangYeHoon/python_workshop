from service.product_service import ProductService
from view.view import message_display, list_display

class ProductController:
    service = ProductService()
    def register(self, product):
        msg = self.service.register(product)
        message_display(msg)
    
    def getAllProduct(self):
        products = self.service.getAllProduct()
        list_display(products)
    
    def update(self, p_id, description):
        if p_id == "" or description == "":
            message_display("공백을 입력하셨습니다.")
        else:
            msg = self.service.update(p_id, description)
            message_display(msg)
    
    def remove(self, p_id):
        if p_id == "":
            message_display("공백을 입력하셨습니다.")
        else:
            msg = self.service.remove(p_id)
            message_display(msg)

    def file_read(self):
        self.service.file_read()
    
    def file_write(self):
        self.service.file_write()