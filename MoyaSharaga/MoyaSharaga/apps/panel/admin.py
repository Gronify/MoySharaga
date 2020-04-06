from django.contrib import admin

# import models
from .models import University, Faculty, Department, Specialty, Group, Student, Teacher, Subject, Mark, ConnectionTSG, Timetable, UserStudent


class UserStudentAdmin(admin.ModelAdmin):
    list_display = ("student", "user")


class UniversityAdmin(admin.ModelAdmin):
    list_display = ("university_short_title", "university_title")


class FacultyAdmin(admin.ModelAdmin):
    list_display = ("faculty_short_title", "faculty_title", "university")


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_short_title", "department_title", "faculty")


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("specialty_title", "department")


class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_title", "specialty")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_surname", "student_name", "student_patronymic", "group")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_surname", "teacher_name", "teacher_patronymic", "teacher_position", "teacher_degree")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_title", "specialty")


class MarkAdmin(admin.ModelAdmin):
    list_display = ("subject", "student", "mark_title", "mark_datetime")


class ConnectionTSGAdmin(admin.ModelAdmin):
    list_display = ("teacher", "group", "subject")


class TimetableAdmin(admin.ModelAdmin):
    list_display = ("group", "subject", "subject_datetime_start", "subject_datetime_stop")


admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(ConnectionTSG, ConnectionTSGAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(UserStudent, UserStudentAdmin)
