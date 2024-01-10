from django.shortcuts import redirect, render
from .models import Member
from django.db.models import Q  # Import Q for complex queries


def index(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        mem = Member.objects.filter(
            Q(firstname__icontains=query) |  # Case-insensitive search for first name
            Q(lastname__icontains=query) |  # Case-insensitive search for last name
            Q(country__icontains=query)  # Case-insensitive search for country
        )
    else:
        mem = Member.objects.all()

    return render(request, 'index.html', {'mem': mem, 'query': query})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")

