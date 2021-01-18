# def 함수명([argumentlist]):
#   구현
#   [return data]
# 함수는 정의 --> 함수 호출
# 함수 호출시 정의된 함수의 argumentlist에 맞도록 데이터 전달

def print_3_times(*value):
    for i in range(0, 3):
        print("{0} : hello functionl {1}".format(i, value))

# 함수호출
print_3_times('test', 'test')
print_3_times('test')

def argument_test(a, b=10, c=20):
    print("{0} : {1} : {2}".format(a, b, c))

argument_test(10)
argument_test(b=200, c=300, a=100)
argument_test(1000, 2000, 3000)

def return_none_test():
    return 

print(return_none_test())

def return_test(a, b):
    sum = a + b
    return sum

print(return_test(10, 20))

def mul(*values):
    result = 1
    for value in values:
        result *= value
    return result

print(mul(5, 7, 9, 10))

# tuple : 값 변경하지 않는 list tuple변수=(value, value, ...)
tuple_data = (10, 20, 30, 40, 50)
list_data = [10, 20, 30, 40, 50]

for tdata in tuple_data:
    print(tdata, end=" ")
print()
for ldata in list_data:
    print(ldata, end=" ")
print()

list_data[0] = 100
# tuple_data[0] = 100 # TypeError : 값 변경할 수 없음
# tuple : function에서 다수의 데이터 리턴시 사용
def test_tuple():
    return (10, 20)

a, b = test_tuple()
a = 30
print("{0} + {1} = {2}".format(a, b, a+b))

# 람다 : lambda argumentlist:return - 1회성 익명함수
list_input = [1, 2, 3, 4, 5]
output_list = map(lambda data:data*data, list_input)
print(list_input)
print(output_list)
print(list(output_list))
output_filter = filter(lambda data: data >= 3, list_input)
print(list_input)
print(output_filter)
print(list(output_filter))