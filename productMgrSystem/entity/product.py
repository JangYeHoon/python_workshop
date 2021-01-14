class Product:
    def __init__(self, p_id, p_name, price, description):
        self.p_id = p_id
        self.p_name = p_name
        self.price = price
        self.description = description
    
    def __eq__(self, p_id):
        return self.p_id == p_id

    def __str__(self):
        return "아이디 : {} 이름 : {} 가격 : {} 설명 : {}".format(self.p_id, self.p_name, self.price, self.description)