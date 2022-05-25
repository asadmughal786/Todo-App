import email
from email import message
from django.contrib import messages
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from .models import TODOS
from .models import Product
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,"base.html")
 
def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(f"{email} {phone} {address}")
        contact = Contact(email = email, phone = phone, address = address)
        user = contact.objects.get()
        contact.save()
        return redirect('contact_us')
    content = Contact.objects.all()
    return render(request, 'contact.html', {"content":content})

def about(request):
    return render(request,"about.html")

def to_does(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        contnt= request.POST.get('contnt')
        to_does = TODOS(title = title,contnt = contnt)
        to_does.save()
        print(f"{title} {contnt}")
        return redirect('to_do')
    dos_content = TODOS.objects.all()
    return render(request, "todoes.html",{"dos_content":dos_content})

def remove(request, pk):
    item = TODOS.objects.get(id = pk)
    item.delete()
    return redirect("to_do")

def markcomp(request, id):
    item = TODOS.objects.get(id = id)
    item.completed= True
    item.save()
    return redirect("to_do")

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        con_password = request.POST.get('con_pass')
        print(f"{name} , {mail}, {password},{con_password}")
        user = User.objects.filter(email = mail).first()
        if user:
            messages.info(request, "User Already Exist....")
            return redirect('sign_up')
        if password == con_password:
            user = User(email = mail, username = mail, first_name = name)
            user.set_password(password)
            user.save()
            messages.info(request,"User saved successfully!")
            return redirect('home')
        else:
            messages.warning(request, 'Passwords are different')
            return redirect('sign_up')
    return render(request,"sign_up.html")

def Product(request):
    if request.method == 'POST':
        prd_ID = request.POST.get('prd_ID')
        prd_name = request.POST.get('prd_name')
        prd_comp_name = request.POST.get('prd_comp_name')
        comp_email = request.POST.get('comp_email')
        comp_contact = request.POST.get('comp_contact')
        contact = Product(prd_name = prd_name, prd_comp_name = prd_comp_name, comp_contact = comp_contact,comp_email=comp_email)
        user = contact.objects.get()
        contact.save()

        return redirect('contact_us')
    content = Contact.objects.all()
    return render(request, 'contact.html', {"content":content})