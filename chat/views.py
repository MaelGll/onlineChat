from django.shortcuts import render, redirect

# Create your views here.
def lobby(request):
    if request.user.is_authenticated:
        return render(request, "chat/lobby.html")
    else :
        return redirect("/")

    
def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, "chat/room.html", {"room_name": room_name})
    else :
        return redirect("/")