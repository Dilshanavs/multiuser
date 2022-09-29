from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,'home.html')

def signup(request):
    form=UserCreationForm()
    if(request.method=="POST"):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'signup.html',{'form':form})

def signup1(request):

    if(request.method=="POST"):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return home(request)
    return render(request,'signup1.html')
