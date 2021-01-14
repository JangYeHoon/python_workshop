from exception.duplicate_exception import DuplicateException
from exception.idnot_found_exception import IDNotFoundException
from dao.todo_file import file_read, file_write

class TodoService:
    todos = []

    # 일정 등록
    def register(self, todo):
        if self.is_exist(todo.todoNum) < 0:
            TodoService.todos.append(todo)
            return "{0}(이)가 등록되었습니다.".format(todo.title)
        else:
            try:
                raise DuplicateException(todo.todoNum)
            except DuplicateException as inputError:
                return str(inputError)

    # 일정 목록
    def getAllTodos(self):
        return TodoService.todos

    # 일정 삭제
    def remove(self, todoNum):
        index = self.is_exist(todoNum)
        if index >= 0:
            TodoService.todos.pop(index)
            return "{}가 삭제되었습니다.".format(todoNum)
        else:
            try:
                raise IDNotFoundException(todoNum)
            except IDNotFoundException as removeError:
                return str(removeError)

    # 일정 리스트 전체 삭제
    def clear(self):
        TodoService.todos.clear()
        return "일정이 모두 삭제되었습니다."
    
    def is_exist(self, todoNum):
        for index, todo in enumerate(TodoService.todos):
            if todo.todoNum == todoNum:
                return index
        return -1
    
    def file_read(self):
        TodoService.todos = file_read()

    def file_write(self):
        file_write(TodoService.todos)