from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.CharField(max_length=10,unique=True)
    stu_name = models.CharField(max_length=20)
    stu_password = models.CharField(max_length=20)
    stu_gender = models.CharField(max_length=2)
    stu_college = models.CharField(max_length=20)
    stu_label1 = models.BooleanField()
    stu_label2 = models.BooleanField()
    stu_label3 = models.BooleanField()
    stu_label4 = models.BooleanField()
    stu_label5 = models.BooleanField()
    stu_label6 = models.BooleanField()

class Course(models.Model):
    cour_id = models.CharField(max_length=10,unique=True)
    cour_name = models.CharField(max_length=20,unique=False)
    cour_teacher = models.CharField(max_length=20)
    cour_timeplace = models.CharField(max_length=30)
    cour_college = models.CharField(max_length=20)
    cour_stunum = models.IntegerField()
    cour_score = models.FloatField()#课程评分
    cour_avescore=models.FloatField()#学生成绩平均分
    cour_failrate=models.FloatField()

class Courseselection(models.Model):
    sel_stu = models.ForeignKey(Student,to_field="stu_id",related_name="studentset",on_delete="CASCADE")
    sel_cour = models.ForeignKey(Course,to_field="cour_id",related_name="courseset",on_delete="CASCADE")
    sel_time = models.DateTimeField()
    sel_score = models.FloatField()#该学生对该课程评价
    sel_grade = models.FloatField()#该学生该门课程的成绩

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_courid = models.ForeignKey(Course,to_field="cour_id",related_name="courseset1",on_delete="CASCADE")
    group_leader = models.ForeignKey(Student,to_field="stu_id",related_name="studentset0",on_delete="CASCADE")
    group_name = models.CharField(max_length=10)
    group_member1 = models.ForeignKey(Student,to_field="stu_id",related_name="studentset1",on_delete="CASCADE",
                                      null=True)
    group_member2 = models.ForeignKey(Student,to_field="stu_id",related_name="studentset2",on_delete="CASCADE",
                                      null=True)
    group_member3 = models.ForeignKey(Student,to_field="stu_id",related_name="studentset3",on_delete="CASCADE",
                                      null=True)
    group_member4 = models.ForeignKey(Student,to_field="stu_id",related_name="studentset4",on_delete="CASCADE",
                                      null=True)

class File(models.Model):
    file_renname = models.CharField(max_length=20,null=True)
    file_filename = models.CharField(max_length=50,null=True)
    file_groups = models.CharField(max_length=10,null=True)
    file_time = models.DateTimeField(null=True)

class Courselog(models.Model):
    log_stu = models.ForeignKey(Student,to_field="stu_id",related_name="logstudentset",on_delete="CASCADE")
    log_cour = models.ForeignKey(Course,to_field="cour_id",related_name="logcourseset",on_delete="CASCADE")
    log_operate=models.CharField(max_length=6)
    log_time = models.DateTimeField()
