from django.shortcuts import render
from .models import OurTeam, Testimony
# Create your views here.

def homepage(request):
    testimony = Testimony.objects.all().order_by("date_created")
    context = {"testimonies": testimony}
    return render(request, "index.html", context)

def about(request):
    team = OurTeam.objects.get(name="John Maxwell").specialization
    # print(team)
    team = OurTeam.objects.all().order_by("date_added")
    context = {"team_members" : team}
    # print(context)
    return render(request, "about.html", context)

def contact(request):
    return render(request, "contact.html")

def prayer_request(request):
    return render(request, "prayer-request.html")

# Areas of Specialisation

def children(request):
    return render(request, "areas/children.html")