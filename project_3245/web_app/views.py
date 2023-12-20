from django.shortcuts import render, HttpResponse

def index_function(request):

   return render(request, 'index.html')

def about_function(request):

    char = "This is About page where you landed"
    # char2

    return HttpResponse(char)

def community_function (request):
   return render (request, 'community.html')