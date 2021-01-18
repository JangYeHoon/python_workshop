# text data file 출력
# write_file = open("hello.txt", 'w')
# write_file.write("Hello Python...\n")
# write_file.close()

# # 자동으로 자원반납
# # mode : 'w'(overwrite), 'a'(append write), 'r'(read)
# with open("hello.txt", 'a') as file:
#     file.write("File Write Test")

# # file read => console 출력
# with open("hello.txt", 'r') as read_file:
#     print("hello.txt 파일 내용 : ", read_file.read())

# # console 입력 => file 출력
# read_data = input("파일에 저장할 데이터 입력 : ")
# with open("console_input.txt", 'w') as f:
#     f.write(read_data)

# file 입력 => file 출력(file copy)
# file_read = open("console_input.txt", 'r')
# file_copy = open("console_input_copy.txt", 'w')
# file_copy.write(file_read.read())
# file_read.close()
# file_copy.close()

import random
hanguls = list("가나다라마바사아자카타파하")
with open("info.txt", "w") as file:
    for i in range(10):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")
        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / (int(height) * int(height))

        result = ""
        if 25 <= bmi:
            reuslt = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"
        
        print('\n'.join(["이름: {}", "몸무게: {}", "키: {}", "BMI: {}", "결과: {}"]).format(name, weight, height, bmi, result))
        print()