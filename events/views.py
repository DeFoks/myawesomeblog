from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    #Получаем все объекты класса Event
    events = Event.objects
    return render(request, 'events/home.html', {'events': events})