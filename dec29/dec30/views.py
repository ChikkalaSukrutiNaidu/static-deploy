from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'dec30/home.html')

def colleges(request):
    colleges_list = ['SVEW', 'VIT', 'BVRICE']
    return render(request, 'dec30/colleges.html', {'colleges': colleges_list})

def students(request):
    students = Student.objects.all()
    return render(request, 'dec30/students.html', {'students': students})

def address(request):
    return render(request, 'dec30/address.html')



