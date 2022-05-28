#from django.db.models import Q, Count
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from .models import face_pay
from django.views.decorators.csrf import csrf_exempt
from django. contrib import messages 
from django import forms  
from .forms import NameForm
from subprocess import run,PIPE
import sys
#------connecting html-pages using djnago-------#
@csrf_exempt
def pay1(request):
  template2 = loader.get_template('pay.html')
  return HttpResponse(template2.render())

def HowitWorks(request):
  template2 = loader.get_template('How-it-Works.html')
  return HttpResponse(template2.render())

@csrf_exempt
def Home(request):
  template2 = loader.get_template('Home.html')
  return HttpResponse(template2.render())

@csrf_exempt
def register(request):
  template2 = loader.get_template('register.html')
  return HttpResponse(template2.render())

@csrf_exempt
def paydone(request):
  template2 = loader.get_template('paydone.html')
  return HttpResponse(template2.render())

def regdone(request):
  template2 = loader.get_template('regdone.html')
  return HttpResponse(template2.render())

#------Validating-Credential-With-Database-------#  
@csrf_exempt
def facelogin(request):
   facepay=face_pay.objects.order_by('Password')
   form = NameForm(request.POST)
   context_dict={'form': form,'facepay': facepay}
   if request.method == 'POST':
       print('valid')
       self=face_pay.objects.get(Password=request.POST.get('psw'))
       form = NameForm(request.POST,self=self)
       if form.is_valid():
          print('valid')  
          if request.POST.get("Name2").strip() == self.Name:
              return redirect(request,'f.html')
       else:
        form = NameForm()   
   return render(request,'pay.html',context_dict,context)

#------Connecting Python-File-Using-Djnago-------#
def external(request): 
    out=run([sys.executable,'members\\templates\\recognition.py'],shell=False,stdout=PIPE)
    stdout_as_str = out.stdout.decode("utf-8")
    print(out)
    return render(request,'paydone.html',{'data1':stdout_as_str})

#------Storing-Data-Of-Registraition-Form-In-MysqlDatabase-------#
@csrf_exempt
def insert(request):
    if request.method == "POST":
        o_ref = face_pay()
        o_ref.Name= request.POST.get('Name1')
        o_ref.Password= request.POST.get('psw')
        o_ref.Picture = request.FILES['image']
        o_ref.save()
        return render(request,'regdone.html') 