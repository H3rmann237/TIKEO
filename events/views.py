from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from django.contrib import messages
from .forms import EventForm

# Create your views here.
# EVENTS = [
#     {"id":1, "nom":"hermann"},
#     {"id":2, "nom":"sammy"},
#     {"id":3, "nom":"rodrigue"}
# ]

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Evenement créee.")
            return redirect("events:event_list")

    else:
        form = EventForm()
    return render(request, "events/event_form.html", {"form": form, "mode": "create"})

def hello(request):
    return HttpResponse("Bonjour Django")

def event_list(request):
    events = Event.objects.all()
    context = {"events" : events}
    return render(
        request,
        "events/events_list.html",
        context
    )
