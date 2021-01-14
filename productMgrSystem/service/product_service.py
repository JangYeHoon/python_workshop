from exception.duplication_exception import DuplicateException
from exception.record_not_found_exception import RecordNotFoundException
from dao.product_file import file_write, file_read

class ProductService:
    products = []
    # 상품 등록
    def register(self, product):
        if self.is_exist(product.p_id) < 0:
            ProductService.products.append(product)
            return "{}(이)가 등록되었습니다.".format(product.p_name)
        else:
            try:
                raise DuplicateException(product.p_name)
            except DuplicateException as inputError:
                return str(inputError)

    # 전체 상품
    def getAllProduct(self):
        return ProductService.products

    # 상품 설명 업데이트
    def update(self, p_id, description):
        index = self.is_exist(p_id)
        if index >= 0:
            ProductService.products[index].description = description
            return "{}의 상품 정보가 수정되었습니다.".format(p_id)
        else:
            try:
                raise RecordNotFoundException(p_id)
            except RecordNotFoundException as updateError:
                return str(updateError)

    # 상품 삭제
    def remove(self, p_id):
        index = self.is_exist(p_id)
        if index >= 0:
            ProductService.products.pop(index)
            return "{}의 상품을 삭제하였습니다.".format(p_id)
        else:
            try:
                raise RecordNotFoundException(p_id)
            except RecordNotFoundException as removeError:
                return str(removeError)

    def is_exist(self, p_id):
        for index, product in enumerate(ProductService.products):
            if product.p_id == p_id:
                return index
        return -1

    # 파일 불러오기
    def file_read(self):
        ProductService.products = file_read()
    
    # 파일 저장
    def file_write(self):
        file_write(ProductService.products)