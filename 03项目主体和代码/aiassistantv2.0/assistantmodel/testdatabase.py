
from django.test import TestCase
from assistantmodel.models import Student,Course,Group,Courseselection,Group,File

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(stu_id="9999999999",stu_name="单元测试",stu_password="123456",
                              stu_gender="男",stu_college="计算机学院",stu_label1=1,stu_label2=1,
                              stu_label3=0,stu_label4=0,stu_label5=1,stu_label6=0)

    def test_students_can_speak(self):
        test1 = Student.objects.get(stu_id="9999999999")
        self.assertEqual(test1.stu_password,"123456")

    def test_login2(self):
        response=self.client.post('/login-post',{'id':'9999999999','password':'123456'})
        self.assertEqual(response.status_code,200)

