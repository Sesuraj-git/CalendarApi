from django.contrib import admin

# Register your models here.
from api.models import Url, Department, Teacher, Class, Student, User, Subject
from api.models import DayOrder, Today, PersonnelStudentEvent, DepartmentEvent, CollegeEvent

admin.site.register(User)
admin.site.register(Url)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(DayOrder)
admin.site.register(Today)
admin.site.register(PersonnelStudentEvent)
admin.site.register(DepartmentEvent)
admin.site.register(CollegeEvent)
admin.site.register(Subject)
