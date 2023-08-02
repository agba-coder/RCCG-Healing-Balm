from django.shortcuts import redirect, render
from django.contrib import messages
from .models import OurTeam, Testimony, Mail
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
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        
        mail = Mail.objects.create(name=name, email=email, subject=subject, message=message)
        mail.save()
        messages.success(request, "Your request has been received and processed successfully. Your message wiil be responded to when received. Thank you😁✅")
        return redirect("contact")
    return render(request, "contact.html")

def prayer_request(request):
    return render(request, "prayer-request.html")

def services(request):
    return render(request, "services.html")

# Areas of Specialisation

def children(request):
    return render(request, "areas/children.html")