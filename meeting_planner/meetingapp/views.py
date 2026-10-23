from django.shortcuts import render, get_object_or_404
from meetingapp.models import Meeting


# Create your views here.
def index(request):
    return render(request,"index.html")

def get_spotkanie(request, id):
    spotkanie = get_object_or_404(Meeting,id=id)
    return render(request,"spotkanie.html", {"spotkanie":spotkanie})


