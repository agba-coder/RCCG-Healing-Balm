from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def prayer_request(request):
    return render(request, "prayer-request.html")