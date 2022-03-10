from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class User(User):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = " 8. User"


class Url(models.Model):
    higrade = models.URLField(blank=False)
    moodle = models.URLField(blank=False)
    home = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = " 7. College URLS"


class Department(models.Model):
    name = models.CharField(max_length=360, blank=False)
    UG = "UG"
    PG = "PG"
    RESEARCH = "RESEARCH"

    CHOICES = (
        (UG, UG),
        (PG, PG),
        (RESEARCH, RESEARCH)
    )
    graduation = models.CharField(max_length=360, choices=CHOICES, default=UG)
    head = models.CharField(max_length=360, blank=False)

    def __str__(self):
        return str(self.name) + " " + str(self.graduation)

    class Meta:
        verbose_name_plural = " 6. Departments"


class Teacher(models.Model):
    staff_id = models.CharField(max_length=360, blank=False)
    name = models.CharField(max_length=360, blank=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.staff_id) + " " + str(self.department.name)

    class Meta:
        verbose_name_plural = " 2. Teachers"


class Class(models.Model):
    class_id = models.CharField(max_length=360, blank=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.class_id) + " " + str(self.department.name) + " " + str(self.class_teacher.staff_id)

    class Meta:
        verbose_name_plural = " 3. Classes"


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    student_id = models.CharField(max_length=360, blank=False)
    name = models.CharField(max_length=360, blank=False)
    email = models.TextField(blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.student_id)


    class Meta:
        verbose_name_plural = " 5. Students"


class Subject(models.Model):
    name = models.CharField(max_length=360, blank=True)
    sub_id = models.CharField(max_length=360, blank=False)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.sub_id) + " " + str(self.class_id.class_id)

    class Meta:
        verbose_name_plural = "12. Subjects"


class DayOrder(models.Model):
    dayorder = models.IntegerField(blank=False)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    hour1 = models.CharField(max_length=360)
    hour2 = models.CharField(max_length=360)
    hour3 = models.CharField(max_length=360)
    hour4 = models.CharField(max_length=360)
    hour5 = models.CharField(max_length=360)
    hour6 = models.CharField(max_length=360)

    def __str__(self):
        return str(self.class_id.class_id) + " " + "DO(" + str(self.dayorder) + ")"

    class Meta:
        verbose_name_plural = " 4. Time Table"


class Today(models.Model):
    date = models.DateField(auto_now=True)
    day_order = models.IntegerField(blank=False, validators=[MaxValueValidator(6), MinValueValidator(1)])

    def __str__(self):
        return str(self.date) + ", " + str(self.day_order)

    class Meta:
        verbose_name_plural = " 1. Today's DayOrder"


class CollegeEvent(models.Model):
    type = models.CharField(max_length=360, blank=True)
    name = models.CharField(max_length=360, blank=False)
    description = models.CharField(blank=True, max_length=1024)

    class Meta:
        verbose_name_plural = "11. College Events"


class DepartmentEvent(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=360, blank=True)
    name = models.CharField(max_length=360, blank=False)
    description = models.CharField(blank=True, max_length=1024)

    class Meta:
        verbose_name_plural = "10. Department Events"


class PersonnelStudentEvent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=360, blank=True)
    event_name = models.CharField(max_length=360, blank=False)
    description = models.CharField(blank=True, max_length=1024)

    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    SELFCOMPLETE = "MARKED AS COMPLETE"

    STATUS = (
        (COMPLETED, COMPLETED),
        (PENDING, PENDING),
        (SELFCOMPLETE, SELFCOMPLETE)
    )

    OPTION = (
        (COMPLETED, COMPLETED),
        (SELFCOMPLETE, SELFCOMPLETE)
    )
    option = models.CharField(max_length=360, choices=OPTION, default=SELFCOMPLETE)
    status = models.CharField(max_length=360, choices=STATUS, default=PENDING)

    class Meta:
        verbose_name_plural = " 9. Student Personnel Event"
