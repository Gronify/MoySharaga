from django.urls import path

from . import views

app_name = 'panel'
urlpatterns = [

        path('', views.index, name = 'index'), # search page
        path('student_id=<int:student_id>/', views.student, name = 'student'), # student page
        path('timetable_id=<int:timetable_id>/', views.timetable, name = 'timetable'), # timetable page(need a rework)
        path('time_new', views.time_new, name = "time_new"), # time_new page for cretaing tables
        path('adding_id=<int:adding_id>/', views.adding, name="adding"),
        path('choice', views.choice, name="choice"),

]
