hello="   Hello Python   "
num_string = input("숫자 입력 : ")
print(hello[1:3])
print(len(hello))
print("문자열 '안녕하세요' 길이는 {0} 입니다.".format(len(hello)))
print(hello.upper())
print(hello.lower())
print(hello.strip())
print("{0}이 숫자인가? {1}".format(num_string, num_string.isdecimal()))
if (num_string.isalnum()):
    num = 10 + int(num_string)

print("'l' 문자열 검색 ", hello.find("l"))
print("'l' 문자열 검색 ", hello.rfind("l"))
print("'l' 문자열 포함여부 ", ("l" in hello))
print(hello.split(" "))