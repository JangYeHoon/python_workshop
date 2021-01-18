# if 조건식 :
#     참일때 실행
# elif 조건식2 :
#     조건식2가 참일때 실행
# else :
#     조건식 1, 2 모두 거짓일때 실행
# month = input("월 입력 : ")
# if month.isdecimal() :
#     m = int(month)
#     if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#         print("{0}의 마지막일은 31일입니다.".format(m))
#     elif m == 2:
#         print("{0}의 마지막일은 31일입니다.".format(m))
#     elif m == 4 or m == 6 or m == 9 m == 11:
#         print("{0}의 마지막일은 30일입니다.".format(m))
#     else:
#         month = input("월은 1~12사이 값을 입력 : ")
# else :
#     month = input("월은 1~12사이 값을 입력 : ")

# list type : [str, int, float, bollean, list], [[1,2,3], [1,2]]
#           +, *(iteration)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b, " +연산후 list_a: ", list_a)
print(list_a.append(4), "append후 list_a ", list_a)
print(list_a.insert(1, 5), "insert(1, 5)후 list_a ", list_a)
print(list_a.pop(1), "pop(1) 삭제 후 list_a", list_a)
print(list_a.remove(1), "remove(1) 1인 값 삭제 후 list_a", list_a)

# for 반복문 in 반복할 수 있는 데이터(list, dictionary, string)
#  실행문
index = 0
for data in list_a:
    print(index, data)
    index += 1