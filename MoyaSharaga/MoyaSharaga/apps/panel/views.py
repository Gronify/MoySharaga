from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required # form for auth

from .forms import TimetableForm
from .models import University, Student, Group, Timetable

# Home Page view
def home_view(request):
    return render(request, 'base.html')

# Search page view
def index(request):
    if request.GET.get("search"):
        search = request.GET.get("search")
        students_search = Student.objects.filter(student_surname = search)
        return render(request, 'results.html', {'students_search': students_search})
    else:
        return render(request, 'search.html')

# Student info page view
@login_required
def student(request, student_id):
    try:
        student = Student.objects.get(id = student_id)
    except:
        raise Http404("Студент не найден")
    return render(request, 'student.html', {'student': student})

# Timetable view(need a rework)
@login_required
def timetable(request, timetable_id):
    try:
        timetableForMonday = Timetable.objects.filter(group_id = timetable_id, day = "M")
        timetableForTuesday = Timetable.objects.filter(group_id = timetable_id, day = "T")
        timetableForWendsday = Timetable.objects.filter(group_id = timetable_id, day = "W")
        timetableForThursday = Timetable.objects.filter(group_id = timetable_id, day = "TH")
        timetableForFriday = Timetable.objects.filter(group_id = timetable_id, day = "F")
        timetableForSaturday= Timetable.objects.filter(group_id = timetable_id, day = "S")
    except:
        raise Http404("Расписание не найдено")
    return render(request, 'timetable.html', {'timetableForMonday': timetableForMonday, 'timetableForTuesday': timetableForTuesday, 'timetableForWendsday': timetableForWendsday, 'timetableForThursday': timetableForThursday, 'timetableForFriday': timetableForFriday, 'timetableForSaturday': timetableForSaturday}, )

# Creating Timetable view
@login_required
def time_new(request):
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            timetable = form.save()
            timetable.save()
            return render(request, 'time_new.html', {'form': form})
    else:
        form = TimetableForm()
        return render(request, 'time_new.html', {'form': form})
