from django.shortcuts import render, HttpResponse

def index_function(request):

   return render(request, 'index.html')

def about_function(request):

   return render(request, 'index.html')

def community_function (request):
   return render (request, 'community.html')

def latest_project (request):
   return render (request, 'latest_project.html')

def signup (request):
   return render (request, 'signup.html')

def signin (request):
   return render (request, 'signin.html')