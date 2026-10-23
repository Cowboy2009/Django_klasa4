from django.shortcuts import render
from .models import Wizyta, Pacjent


# Create your views here.
def home(request):
    wizyty = Wizyta.objects.all()
    pacjenci = Pacjent.objects.all()
    return render(request, "home.html", context={"wizyty": wizyty, "pacjenci": pacjenci})