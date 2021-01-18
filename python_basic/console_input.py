hello = input("인사말 입력 : ")
print(hello, type(hello))
print("입력하신 인사말은 {0} 입니다.".format(hello))

data = input("숫자 입력 : ")
print(data, type(data))
print("입력한 숫자는 {0}이고 타입은 {1}입니다.".format(data, type(data)))

x = 100
# sum = x + data # type error
sum = x + int(data) # type cast
print("sum : ", sum)
sum = 10 + 10.5
print(type(sum))