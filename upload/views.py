from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AssignmentForm
from .models import Assignment

def index(request):
    form = AssignmentForm()
    return render(request, 'index.html', {'form' : form}  )

def create(request):
    form = AssignmentForm()
    if request.method=="POST":
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            print("form valid")
            form.save()
            print("save")
        else:
            redirect('index')    
            print("nono")
    return redirect('index')

# @login_required
def teacher_admin(request):
    assignments = Assignment.objects.all().order_by('-timestamp')
    return render(request, 'teacher_admin.html', {'assign': assignments})