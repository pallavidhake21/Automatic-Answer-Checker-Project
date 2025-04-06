from django.shortcuts import redirect, render
from .models import Answer, Exam,Registration
# Create your views here.
def test(request):
    exam = Exam.objects.all()
    return render(request, "test.html",{'exam': exam})
        
# Create your views here.
def login(request):
    return render(request, "login.html")
def start(request):
    return render(request, "start.html")
def mjc(request):
    if request.method == "POST":
        data = Registration()
        data.Fname = request.POST.get('firstname')
        data.mname = request.POST.get('middlename')
        data.lname = request.POST.get('lastname')
        data.choice = request.POST.get('choice')
        data.Gender = request.POST.get('gender')
        data.number = request.POST.get('phone')
        data.Address = request.POST.get('address')

        data.save()

        return redirect('/login/')
    else:
        return render(request, "mjc.html") 
def about(request):
    return render(request, "about.html")                
def contact(request):
    return render(request, "contact.html")  
def instruction(request):
    return render(request, "instruction.html")  
def logout(request):
    return render(request, "logout.html")  