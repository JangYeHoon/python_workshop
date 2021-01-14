from service.todo_service import TodoService
from view.view import message_display, list_display

class TodoController:
    service = TodoService()
    def register(self, todo):
        msg = self.service.register(todo)
        message_display(msg)
    
    def getAllTodos(self):
        todos = self.service.getAllTodos()
        list_display(todos)
    
    def remove(self, todoNum):
        if todoNum == "":
            message_display("공백 문자를 입력하셨습니다.")
        msg = self.service.remove(todoNum)
        message_display(msg)
    
    def clear(self):
        msg = self.service.clear()
        message_display(msg)
    
    def file_read(self):
        self.service.file_read()

    def file_write(self):
        self.service.file_write()