from django.db import migrations, models
import django.db.models.deletion


# Create your models here.
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_text = models.TextField()
    correct_answer = models.IntegerField()
    question = models.ForeignKey('Question', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'answer'


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    number_of_points = models.IntegerField()
    weight = models.IntegerField(blank=True, null=True)
    question_type = models.ForeignKey('QuestionType', models.DO_NOTHING)
    test = models.ForeignKey('Test', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionType(models.Model):
    question_type_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'question_type'


class Student(models.Model):
    student = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(unique=True, max_length=25)
    subject_details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    final_grade = models.IntegerField()
    test = models.ForeignKey('Test', models.DO_NOTHING)
    student = models.ForeignKey(Student, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'submission'


class Submittedanswer(models.Model):
    submitted_answer_id = models.AutoField(primary_key=True)
    submitted_answer_open_question = models.TextField(blank=True, null=True)
    assigned_grade = models.IntegerField(blank=True, null=True)
    submission = models.ForeignKey(Submission, models.DO_NOTHING)
    answer = models.ForeignKey(Answer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'submittedanswer'


class Teacher(models.Model):
    teacher = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'teacher'


class TeacherSubject(models.Model):
    teacher_subject_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teacher_subject'


class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(unique=True, max_length=45)
    test_password = models.CharField(max_length=128, blank=True, null=True)
    test_date = models.DateField()
    test_start_time = models.TimeField()
    test_end_time = models.TimeField()
    max_score = models.IntegerField(blank=True, null=True)
    teacher_subject = models.ForeignKey(TeacherSubject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'test'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email_address = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=25)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'user'
