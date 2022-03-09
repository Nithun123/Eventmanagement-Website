from django.shortcuts import render,redirect


from .models import new_users,Event,details,contact

def login(request):
    return render(request,'login.html')
def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        data = contact(name=name,email=email,message=message)
        print('success')
        data.save()
        return redirect('/')
    else:
        return render(request,'contact.html')



def about(request):
    return render(request,'about.html')
def dashboard(request):
    if request.method == 'POST':
        name = request.POST['ename']
        price = request.POST['eprice']
        data = Event(ename=name,eprice=price)
        print('Success')
        data.save()
        return redirect('/add')
    else:
        return render(request,'dashboard.html')



def shows(request):
    event = Event.objects.all()
    return render(request,'dashshow.html', {'event':event})


def signups(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        data=new_users(name=name, email=email, contact=contact, password=password)
        data.save()

        return redirect('/signin')
    else:
        return render(request,'Usignup.html')



def signin(request):

    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['pass1']
        if new_users.objects.filter(email=email,password=password).exists():
            print("sucess")

            return redirect('/show')

    else:
        return render(request,'signin.html')

def deatils(request):
    if request.method =='POST':
        name = request.POST['name']
        phone = request.POst['phone']
        category = request.POST['category']
        startdate= request.POST['startdate']
        enddate = request.POST['enddate']
        price= request.POST['price']
        place = request.POST['place']
        person = request.POST['person']
        food = request.POST['food']
        time = request.POST['time']
        light = request.POST['lights']
        flower = request.POST['flower']
        seet = request.POST['seet']
        equpment = request.POST['equpment']
        music = request.POST['music']
        data = details(name=name,phone=phone,price=price,category=category,place=place,person=person,startdate=startdate,enddate=enddate,food=food,time=time,
                              light=light,flower=flower,seet=seet,equpment=equpment,music=music)
        data.save()
        return redirect('/details')
    else:
        return render(request,'detail.html' )


def dshow(request):
    detail= details.objects.all()
    return render(request,'detailshow.html',{ 'detail':detail })





def add(request):
    event = Event.objects.all()
    return render(request, 'dashshow2.html', {'event': event})

def delete(request,id):
    event =Event.objects.get(id=id)
    event.delete()
    return redirect("/add")

def Pay(request):
    return render(request,"pay.html")