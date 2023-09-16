from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm,FeedbackForm,ProfileForm
from django.contrib.auth.decorators import login_required
import openai
from django.utils import timezone
from .models import Profile,BotUser,FeedBack

def palak_bot(message):
    openai_key = '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'
    openai.api_key = openai_key
    
    if 'your name' in message:
        answer = 'My name is ChatBox.'

    else:
        message = message.replace('palak',"")
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system","content":"I'm AI assistant..."},
                {"role":"user","content":message},
            ]
        ) 
        print(response)
        answer = response.choices[0].message.content.strip()

    return answer

@login_required(login_url='login/')
def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = palak_bot(message)
        chat = BotUser(profile=request.user,name=request.user.username,prompt=message,response=response,prompt_date=timezone.now())
        chat.save()
        return JsonResponse({'message':message,'response':response})
        
    context = {}
    return render(request,'chatbot.html',context)

@login_required(login_url='login/')
def profile(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('chatbot')
    context = {'form':form}
    return render(request,'profile.html',context)

def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='login/')
def feedback(request):
    form = FeedbackForm(initial={'gender':'Homo Sapiens'})
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        nm = request.POST.get('name')
        em = request.POST.get('email')
        age = request.POST.get('age')
        gd = request.POST.get('gender')
        mb = request.POST.get('phone')
        loc = request.POST.get('location')
        des = request.POST.get('descprition')
        if form.is_valid():
            feed = FeedBack(feed=request.user,name=nm,email=em,phone=mb,descprition=des,gender=gd,location=loc,age=age,created_date=timezone.now())
            feed.save()
            return redirect('chatbot')

    context = {'form':form}
    return render(request,'feedback.html',context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            if form.is_valid():
                try:
                    user = form.save()

                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    Profile.objects.create(user=user,name=username,email=email)

                   
                    return redirect('login')
                except:
                   
                    return render(request,'register.html')

        else:
           
            return render(request,'register.html')

    return render(request,'register.html')

def loginpage(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('chatbot')
        else:
            
            return render(request,'loginpage.html')

    return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect('login')