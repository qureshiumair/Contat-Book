from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import contact
# Create your views here.
def home(request):
    temp=contact.objects.all()


    return render(request,"index.html",{"b":temp})


def add(request):
     if request.method=="POST":
         temp=contact(name=request.POST['fname'],phone=request.POST['phone'],email=request.POST['email'],address=request.POST['address'],relationship=request.POST['relationship'])
         temp.save()
         return redirect("home")
     else:
         return render(request,"new.html")   

def search(request):
    if request.method=="POST":
        temp=request.POST['search']
        
        a=contact.objects.filter(name=temp)
        try:
            return render(request,"index.html",{"b":a})
        except:
            return redirect("home")

    else:
        return render(request,"index.html")    


def profile(request,key):
    key=contact.objects.get(id=key)
    return render(request,"profile.html",{"v":key})            

def edit(request,key):
    
    if request.method=="POST":
        a=contact.objects.get(id=key)
        a.delete()
        temp=contact(name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'],address=request.POST['address'],relationship=request.POST['relationship'])
        temp.save()
        return redirect("home")

              

    else:
        key=contact.objects.get(id=key)
        return render(request,"edit.html",{"a":key})    




def delete(request,key):
     if request.method=="GET":
         a=contact.objects.get(id=key)
         a.delete()
         return redirect("home")       