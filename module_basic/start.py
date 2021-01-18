# import test_package.module_test as test
# import test_package.module_test2 as test2
from test_package import *

radius = module_test.number_input()
print(module_test.get_circumferecne(radius))
print(module_test.get_circle_area(radius))

x, y = module_test2.number_input()
print(module_test2.get_circumferecne(x, y))
print(module_test2.get_rectangle_area(x, y))

print("#메인의 __name__ 출력#")
print(__name__)
print()