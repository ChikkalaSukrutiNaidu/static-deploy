from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def colleges(request):
    return render(request, 'colleges.html')

def students(request):
    data = Student.objects.all()
    return render(request, 'students.html', {'students': data})
