from django import forms

from .models import Timetable, Faculty, Department, Specialty, Student, Teacher, Group, UserStudent, UserTeacher, ConnectionTSG


class UserStudentForm(forms.ModelForm):

    class Meta:
        model = UserStudent
        fields = ('student', 'user',)

class UserTeacherForm(forms.ModelForm):

    class Meta:
        model = UserTeacher
        fields = ('teacher', 'user',)

class ConnectionTSGForm(forms.ModelForm):

    class Meta:
        model = ConnectionTSG
        fields = ('teacher', 'group', 'subject')


# form for timetable
class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = ('group', 'subject', 'day', 'subject_datetime_start', 'subject_datetime_stop',)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('student_surname', 'student_name', 'student_patronymic', 'student_sex', 'group')

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ('teacher_surname', 'teacher_name', 'teacher_patronymic', 'teacher_sex', 'teacher_position', 'teacher_degree')

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ('university', 'faculty_short_title', 'faculty_title')


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('faculty', 'department_short_title', 'department_title')


class SpecialtyForm(forms.ModelForm):

    class Meta:
        model = Specialty
        fields = ('department', 'specialty_title')


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('specialty', 'group_title')
