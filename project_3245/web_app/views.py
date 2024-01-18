from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from web_app.models import signup
from django.contrib import messages

def index_function(request):

   return render(request, 'index.html')

def about_function(request):

   return render(request, 'index.html')

def community_function (request):
   return render (request, 'community.html')

def latest_project (request):
   return render (request, 'latest_project.html')

def signup_view (request):
   if request.method == "POST":
      Fullname = request.POST.get("full_name")
      Phn_number = request.POST.get("phn")
      gender = request.POST.get("gender")
      email = request.POST.get("email")
      Password = request.POST.get("new_password")
      confirm_password = request.POST.get("con_password")
      Userid = request.POST.get("userID")
      Username = request.POST.get("username")
      register_date = request.POST.get("reg_date")

      if (Password != confirm_password):
            messages.error(request, "Password and Confirm Password did not matched.")
            return redirect('/signup')
      
      if (len(Fullname) >=40 ):
         messages.error(request, "Fullname can not be esceed the limit")
         return redirect('/signup')

      if (Password == Fullname):
         messages.error(request, "Password and Name can not be same")
         return redirect ('/signup')
   
      if (len(Phn_number) >= 10):
         messages.error(request, "Phone number can not be greater then 10 digits")
         return redirect ('/signup')
   
      signup_object = signup (fullname = Fullname, phone_number = Phn_number,
      Gender = gender, Email = email, new_password = Password, user_id = Userid,
      username = Username, Reg_date = register_date)
      signup_object.save()
   
      messages.success(request, "Signup successful!")  # Optional success message
      return redirect('/signup')
   
   return render (request, 'signup.html')

def signin (request):
   return render (request, 'signin.html')