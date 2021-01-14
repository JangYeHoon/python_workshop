import os
from entity.todo import Todo

# 프로그램 종료시 list students "students.dat" 파일 저장
def file_write(todos):
    save_file = open("todos.dat", "w")
    for index, todo in enumerate(todos):
        save_file.write("{}번째 | {}, {}\n".format(index, todo.todoNum, todo.title))

    save_file.close()
# 프로그램 시작시 "students.dat" 파일이 존재하고 정보가 있는 경우 list studetns 초기화
def file_read():
    todos = []
    fileExist = os.path.isfile("todos.dat")
    if fileExist:
        read_file = open("todos.dat", "r")
        while True:
            data = read_file.readline()
            if len(data.split("|")) == 2:
                todo = data.split("|")[1].strip("\n").split(', ')
                todos.append(Todo(todo[0].strip(), todo[1]))
            if not data: break
        read_file.close()
    return todos