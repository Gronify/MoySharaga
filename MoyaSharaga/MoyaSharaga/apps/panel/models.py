from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# consts for Student and Teacher models(sex)
NOT_SPECIFIED = 'N'
MALE = 'M'
FEMALE = 'F'

SEX_CHOICES = (
(NOT_SPECIFIED, 'Не указанно'),
(MALE, 'Мужчина'),
(FEMALE, 'Женщина'),
)

# consts for Timetable model(day)
NODAY = 'N/A'
MONDAY = 'M'
TUESDAY = 'T'
WENDSDAY = 'W'
THURSDAY = 'TH'
FRIDAY = 'F'
SATURDAY = 'S'

DAY_CHOICES = (
(NODAY, 'Не выбрано'),
(MONDAY, 'Понедельник'),
(TUESDAY, 'Вторник'),
(WENDSDAY, 'Среда'),
(THURSDAY, 'Четверг'),
(FRIDAY, 'Пятница'),
(SATURDAY, 'Суббота'),
)


# University model
class University(models.Model):
  university_short_title = models.CharField('Название Вуза(Сокращенно)', max_length = 20)
  university_title = models.CharField('Название Вуза', max_length = 200)

  def __str__(self):
    return self.university_short_title

    class Meta:
      verbose_name = 'ВУЗ'
      verbose_name_plural = 'ВУЗЫ'


# Faculty model
class Faculty(models.Model):
  university = models.ForeignKey(University, on_delete = models.CASCADE)
  faculty_short_title = models.CharField('Название Факультета(Сокращенно)', max_length = 20)
  faculty_title = models.CharField('Название Факультета', max_length = 200)

  def __str__(self):
    return self.faculty_short_title

    class Meta:
      verbose_name = 'Факультет'
      verbose_name_plural = 'Факультеты'


# Department model
class Department(models.Model):
  faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
  department_short_title = models.CharField('Название Кафедры(Сокращенно)', max_length = 20)
  department_title = models.CharField('Название Кафедры', max_length = 200)

  def __str__(self):
    return self.department_short_title

    class Meta:
      verbose_name = 'Кафедра'
      verbose_name_plural = 'Кафедры'


# Specialty model
class Specialty(models.Model):
  department = models.ForeignKey(Department, on_delete = models.CASCADE)
  specialty_title = models.CharField('Название Специальности', max_length = 200)

  def __str__(self):
    return self.specialty_title

    class Meta:
      verbose_name = 'Специальность'
      verbose_name_plural = 'Специальности'


# Group model
class Group(models.Model):
  specialty = models.ForeignKey(Specialty, on_delete = models.CASCADE)
  group_title = models.CharField('Название Группы', max_length = 50)

  def __str__(self):
    return self.group_title

    class Meta:
      verbose_name = 'Группа'
      verbose_name_plural = 'Группы'


# Student model
class Student(models.Model):

  student_surname = models.CharField('Фамилия', max_length = 200)
  student_name = models.CharField('Имя', max_length = 200)
  student_patronymic = models.CharField('Отчество', max_length = 200)
  student_sex = models.CharField('Пол', max_length = 1, choices = SEX_CHOICES, default = NOT_SPECIFIED)
  group = models.ForeignKey(Group, on_delete = models.CASCADE)

  def __str__(self):
    return self.student_surname

    class Meta:
      verbose_name = 'Студент'
      verbose_name_plural = 'Студенты'


# Teacher model v2
class Teacher(models.Model):

  teacher_surname = models.CharField('Фамилия', max_length = 200)
  teacher_name = models.CharField('Имя', max_length = 200)
  teacher_patronymic = models.CharField('Отчество', max_length = 200)
  teacher_sex = models.CharField('Пол', max_length = 1, choices = SEX_CHOICES, default = NOT_SPECIFIED)
  teacher_position = models.CharField('Должность', max_length = 200) # НАПРИМЕР Зав. кафед
  teacher_degree = models.CharField('Научная степень', max_length = 200) # НАПРИМЕР Профессор

  def __str__(self):
    return self.teacher_surname

    class Meta:
      verbose_name = 'Преподаватель'
      verbose_name_plural = 'Преподаватели'


# Subject model v2
class Subject(models.Model):
 specialty = models.ForeignKey(Specialty, on_delete = models.CASCADE)
 subject_title = models.CharField('Название Предмета', max_length = 50)

 def __str__(self):
   return self.subject_title

   class Meta:
     verbose_name = 'Предмет'
     verbose_name_plural = 'Предметы'


# Mark model v1
class Mark(models.Model):
  subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
  student = models.ForeignKey(Student, on_delete = models.CASCADE)
  # maybe mark can be integer/ but we have marks as 'A' 'B' 'F'
  mark_title = models.CharField('Оценка', max_length = 5)
  mark_datetime = models.DateTimeField('Время оценки', default=timezone.now)

  def __str__(self):
    return self.mark_title

    class Meta:
      verbose_name = 'Оценка'
      verbose_name_plural = 'Оценки'


# Connection of Teacher, Subject, Group model v1
class СonnectionTSG(models.Model):

  teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
  group = models.ForeignKey(Group, on_delete = models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete = models.CASCADE)


  def __str__(self):
    return str(self.teacher)

    class Meta:
      verbose_name = 'СonnectionTSG'
      verbose_name_plural = 'СonnectionsTSG'


# Timetable model v2
class Timetable(models.Model):

  group = models.ForeignKey(Group, on_delete = models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
  day = models.CharField('День недели', max_length=3, choices = DAY_CHOICES, default = NODAY)
  subject_datetime_start = models.TimeField('Время начала пары')
  subject_datetime_stop = models.TimeField('Время конца пары')

  def __str__(self):
    return str(self.subject)

    class Meta:
      verbose_name = 'Расписание'
      verbose_name_plural = 'Расписание'


class UserStudent(models.Model):
  student = models.ForeignKey(Student, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.student

  class Meta:
    verbose_name = 'Связь'
    verbose_name_plural = 'Связи'