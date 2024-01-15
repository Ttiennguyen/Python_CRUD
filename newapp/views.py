from django.shortcuts import redirect, render
from .models import Member, Login
from django.db.models import Q  # Import Q for complex queries

# đưa toàn bộ dữ liệu lên
# def index(request):
#     mem= Member.objects.all()
#     return render(request, 'index.html', {'mem': mem})

#đưa toàn bộ dữ liệu có thêm phần tìm kiếm
def index(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        mem = Member.objects.filter(
            Q(email__icontains=query) |  # Case-insensitive search for first name
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
    # Lấy thông tin từ dữ liệu POST gửi từ biểu mẫu thêm thành viên
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    e=request.POST['email']
    a=request.POST['age']
    s=request.POST['salary']
    i=request.POST['image']
    # Tạo đối tượng `Member` mới với thông tin này và lưu vào cơ sở dữ liệu
    mem=Member(firstname=x,lastname=y,country=z,email=e,age=a,salary=s,image=i)
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
    e = request.POST['email']
    a = request.POST['age']
    s = request.POST['salary']
    i = request.POST['image']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.email=e
    mem.age=a
    mem.salary=s
    mem.image=i
    mem.save()
    return redirect("/")

##### Phần login
def indexlogin(request):
    log = Login.objects.all()
    return render(request, 'indexlogin.html', {'log': log})
def addlogin(request):
    return render(request,'addlogin.html')

def addreclogin(request):
    # Lấy thông tin từ dữ liệu POST gửi từ biểu mẫu thêm thành viên
    e=request.POST['email']
    p=request.POST['password']

    log=Login(username=e,password=p)
    log.save()
    return redirect("/indexlogin")

def deleteacc(request,id):
    log=Login.objects.get(id=id)
    log.delete()
    return redirect("/indexlogin")

def loginview(request):
    return render(request, 'login.html')
#ktr pass và tk
def logincheck(request):

    u = request.POST['username']
    p = request.POST['password']

    log = Login(username=u,password=p)

    log1 = Login.objects.filter(username=u).first()

    if log1 and log.password == log1.password:
        return redirect("/indexlogin")
    else:
        return redirect("/loginview")


