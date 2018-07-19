from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def login(request):
    return render(request, 'wall_app/login.html')



def process_registration(request):
    result= User.objects.validate_registration(request.POST)
    if len(result)>0:
        for key in result.keys():
            messages.error(request,result[key])
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
        user= User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], password= hashed_pw)
        request.session['user_id']=user.id
        return redirect('/wall')

def process_login(request):
    user= User.objects.filter(email=request.POST['email'])
    if len(user) == 0:
        messages.error(request,"No user with that email exists")
        return redirect('/')
    else:
        user=user.first()
    password_validation = bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())
    if password_validation:
        request.session['user_id']=user.id
        return redirect('/wall')
    else:
        messages.error(request,"Information is Incorrect")
        return redirect('/')


def index(request):
    the_user= User.objects.get(id=request.session['user_id'])
    all_messages=Message.objects.all()
    all_comments=Comment.objects.all()
    context={
        "user":the_user,  
        "messages":all_messages,
        "comments":all_comments
    }
    # the_message=Message.objects.filter(user=the_user)
    # if len(the_message) != 0:
    #     context['message']=the_message
    # else:
    #     pass
    return render(request,'wall_app/index.html', context)

def create_message(request):
    the_user= User.objects.get(id=request.session['user_id'])
    message= Message.objects.create(user=the_user, content= request.POST['message'])
    return redirect('/wall')

def create_comment(request):
    the_user= User.objects.get(id=request.session['user_id'])
    the_message=Message.objects.get(id=request.POST['post_id'])
    comment= Comment.objects.create(user=the_user, message= the_message ,content= request.POST['comment'])
    return redirect('/wall')

def delete(request, post_id):
    message= Message.objects.get(id=post_id)
    message.delete()
    return redirect('/wall')




