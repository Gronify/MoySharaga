from django.urls import path

from . import views

app_name = 'panel'
urlpatterns = [

        path('', views.index, name = 'index'), # search page
        path('student_id=<int:student_id>/', views.student, name = 'student'), # student page
        path('timetable_id=<int:timetable_id>/', views.timetable, name = 'timetable'), # timetable page(need a rework)
        path('adding_id=<int:adding_id>/', views.adding, name="adding"), # adding url
        path('choice', views.choice, name="choice"), # choice url

]
