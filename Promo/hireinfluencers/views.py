from django.shortcuts import render,redirect
from django.core.checks import messages
from .models import Hiretuber
from django.contrib import messages

# Create your views here.

    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #email = models.CharField(max_length=100)
    #tuber_id = models.IntegerField()
    #tuber_name = models.CharField(max_length=100)
   # city = models.CharField(max_length=100)
   # phone = models.CharField(max_length=100)
   # state = models.CharField(max_length=100)
   # message = models.TextField(blank = True)
   # user_id = models.IntegerField(blank = True)
    #created_date = models.DateTimeField(blank = True, default=datetime.now)
def hiretuber(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        tuber_id=request.POST['tuber_id']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']
        messages.success(request, 'Thanks for Reaching out!')
        hiretuber=Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone, email=email,state=state, message=message,user_id=user_id)
        hiretuber.save()
        return redirect('youtubers')