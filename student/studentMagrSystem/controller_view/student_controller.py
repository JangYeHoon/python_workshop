# 입력데이터 valid 체크, service에 비즈니스 로직 호출, data 저장, view(template) 선택
from service.student_service import StudentService
from view_template.template_view import message_display, list_display

class StudentController:
    service = StudentService()

    def register(self, student):
        # 만약 id가 email 형식인 경우 email 맞는지 student.id vaild 체크
        msg = self.service.register(student)    # 비즈니스 메서드 호출
        message_display(msg)    # View select

    def getAllStudents(self):
        students = self.service.getAllStudents()    # 비즈니스 메서드 호출
        list_display(students)  # 데이터 저장해서 view select

    def update(self, id, major):
        # id, major valid check
        if id  == "" or major == "":
            message_display("공백 문자를 입력하셨습니다.")
        msg = self.service.update(id, major)
        message_display(msg)

    def remove(self, id):
        if id == "":
            message_display("공백 문자를 입력하셨습니다.")
        msg = self.service.remove(id)
        message_display(msg)

    def file_read(self):
        self.service.file_read()

    def file_write(self):
        self.service.file_write()
