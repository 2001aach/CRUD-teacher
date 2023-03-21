
from django.shortcuts import render, redirect

from teacherapp.forms import teacherform
from teacherapp.models import teacher


# Create your views here.

def mainpage(request):
    return render(request,'index.html')

def home(request):
    return render(request,'hm.html')


def view(request):
    data = teacher.objects.all()
    return render(request,'tview.html',{'data':data})


def add(request):
    data=teacher.objects.all()
    form=teacherform()
    if request.method=='POST':
        form=teacherform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'add.html',{'form':form})


