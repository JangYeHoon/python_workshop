class Todo:
    def __init__(self, todoNum, title):
        self.todoNum = todoNum
        self.title = title

    def __eq__(self, todoNum):
        return self.todoNum == todoNum
    
    def __str__(self):
        return "아이디:{0} 일정:{1}".format(self.todoNum, self.title)