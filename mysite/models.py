from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class Skills(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class Industry(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class Country(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class UserType(models.Model):
    type = models.CharField(max_length=50)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.type)

    class Meta:
        ordering = ('type',)

class Title(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class Position(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

class Future_Student(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200, blank=True, null=True)
	date_of_birth = models.DateField()
	email = models.EmailField()
	pin_code = models.CharField(max_length=15, blank=True, null=True, default='')
	address = models.CharField(max_length=500, blank=True, null=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
	highest_degree_obtained = models.CharField(max_length=50, blank=True, null=True)
	grades_obtained = models.CharField(max_length=3, blank=True, null=True)
	max_grades = models.CharField(max_length=3, blank=True, null=True)
	subject_interested = models.ForeignKey(Subjects,on_delete=models.CASCADE)
	is_active = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)

class Students(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200, blank=True, null=True)
	date_of_birth = models.DateField()
	email = models.EmailField()
	pin_code = models.CharField(max_length=15, blank=True, null=True, default='')
	address = models.CharField(max_length=500, blank=True, null=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
	programme_studied = models.CharField(max_length=500)
	grades_obtained = models.CharField(max_length=3, blank=True, null=True)
	max_grades = models.CharField(max_length=3, blank=True, null=True)
	year_of_study = models.IntegerField()
	skills_interested = models.ForeignKey(Skills, on_delete=models.CASCADE)
	industry_interested = models.ForeignKey(Industry, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)

class User_Info(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200, blank=True, null=True)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	position_in_company = models.CharField(max_length=50, blank=True, null=True)
	working_years = models.IntegerField(default=0)
	no_of_employees = models.IntegerField()
	website_url = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=500, blank=True, null=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
	company_registration_number = models.CharField(max_length=500, blank=True, null=True)
	skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
	industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)


class ExistingEmployee(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200, blank=True, null=True)
	date_of_birth = models.DateField()
	position_in_company = models.CharField(max_length=50, blank=True, null=True)
	website_url = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=500, blank=True, null=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
	email = models.EmailField()
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	company_registration_number = models.CharField(max_length=500, blank=True, null=True)
	skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
	industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)


class Teacher(models.Model):
	username = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.ForeignKey(Title,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	email = models.EmailField()
	surname = models.CharField(max_length=200, blank=True, null=True)
	university_name = models.CharField(max_length=200, blank=True, null=True)
	university_address = models.CharField(max_length=500, blank=True, null=True)
	phone_number = models.CharField(max_length=15, blank=True, null=True)
	position = models.ForeignKey(Position,on_delete=models.CASCADE)
	programme_title = models.CharField(max_length=200, blank=True, null=True)
	subject_area = models.ForeignKey(Subjects,on_delete=models.CASCADE)

class Teacher_connections(models.Model):
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	teacher_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_future_students = models.TextField(blank=True, null=True)
	connected_existing_students = models.TextField(blank=True, null=True)

class Future_connections(models.Model):
	future_student_id = models.ForeignKey(Future_Student,on_delete=models.CASCADE)
	future_student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_teachers = models.TextField(blank=True,null=True)


class Teacher_post(models.Model):
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	teacher_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(blank=True, null=True)
	time_stamp = models.DateTimeField(auto_now=True)

class Future_student_post(models.Model):
	future_student_id = models.ForeignKey(Future_Student,on_delete=models.CASCADE)
	future_student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(blank=True, null=True)
	time_stamp = models.DateTimeField(auto_now=True)

class Existing_student_post(models.Model):
	student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
	student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(blank=True, null=True)
	time_stamp = models.DateTimeField(auto_now=True)

class Employee_post(models.Model):
	employee_id = models.ForeignKey(User_Info,on_delete=models.CASCADE)
	employee_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200,null=True)
	description = models.TextField(blank=True, null=True)
	file = models.FileField(blank=True, null=True)
	time_stamp = models.DateTimeField(auto_now=True)


class StudentEmployeeMapping(models.Model):
	student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
	student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_employee_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_employee_id')
	time_stamp = models.DateTimeField(auto_now=True)

class EmployeeStudentMapping(models.Model):
	employee_id = models.ForeignKey(Students,on_delete=models.CASCADE)
	employee_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_student_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_student_id')
	time_stamp = models.DateTimeField(auto_now=True)

class StudentEmployeeNotification(models.Model):
	logged_id = models.ForeignKey(User,on_delete=models.CASCADE)
	logged_type = models.CharField(max_length=200,blank=True,null=True)
	sending_ids = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_ids')
	sending_type = models.CharField(max_length=200,blank=True,null=True)
	pending = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)









class TeacherStudentMapping(models.Model):
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
	teacher_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_student_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_existing_student_id')
	time_stamp = models.DateTimeField(auto_now=True)

class StudentTeacherMapping(models.Model):
	student_id = models.ForeignKey(Students,on_delete=models.CASCADE)
	student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_teacher_user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_teacher_user_id')
	time_stamp = models.DateTimeField(auto_now=True)

class TeacherFutureMapping(models.Model):
	teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True)
	teacher_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_future_student_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_future_student_id')
	time_stamp = models.DateTimeField(auto_now=True)

class FutureTeacherMapping(models.Model):
	future_id = models.ForeignKey(Future_Student,on_delete=models.CASCADE,blank=True,null=True)
	future_student_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	connected_teacher_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='connected_teacher_id')
	time_stamp = models.DateTimeField(auto_now=True)

class TeacherFutureNotifications(models.Model):
	logged_id = models.ForeignKey(User,on_delete=models.CASCADE)
	logged_type = models.CharField(max_length=200,blank=True,null=True)
	sending_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_id')
	sending_type = models.CharField(max_length=200,blank=True,null=True)
	pending = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)


class TeacherStudentNotification(models.Model):
	logged_id = models.ForeignKey(User,on_delete=models.CASCADE)
	logged_type = models.CharField(max_length=200,blank=True,null=True)
	sending_ids = models.ForeignKey(User,on_delete=models.CASCADE,related_name='senders_ids')
	sending_type = models.CharField(max_length=200,blank=True,null=True)
	pending = models.BooleanField(default=1)
	time_stamp = models.DateTimeField(auto_now=True)







