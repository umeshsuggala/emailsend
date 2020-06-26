from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random 
from firstapp.models import Email
from django.http import HttpResponse
from emailsend import settings

# Create your views here.
def index(request):
	if request.method=='POST':
		email=request.POST['email']
		pwd=str(random.randint(100000,999999))
		data=Email(email=email,pwd=pwd)
		data.save()
		sub='Reg to your login deatils'
		body='''Hello \n\n\n  Your Username : {}\n\n 
		Your Paasword is : {}\n\n'''.format(email,pwd)
		reciever=email
		sender=settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[reciever])
		return HttpResponse('Please Check your Email Id')

	return render(request,'index.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		pwd=request.POST['pwd']
		data=Email.objects.filter(email=email,pwd=pwd)
		if data:
			return HttpResponse('Welcome to user')
		else:
			return HttpResponse("Invalid User")
	return render(request,'login.html')

def confirm(request):
	if request.method=='POST':
		email=request.POST['email']
		old=request.POST['old']
		new=request.POST['new']
		new2=request.POST['new2']
		data=Email.objects.filter(email=email,pwd=old)
		
		

		if data:
			if new==new2:
				Email.objects.filter(pwd=old).update(new=new)
				Email.objects.filter(pwd=old).update(pwd=new)
				
				

				return HttpResponse('Done')
			else:
				return HttpResponse('PASSWORD not matched')
		else:
			return HttpResponse('Invalid user')
		
	return render(request,'confirm.html')