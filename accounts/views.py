from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User, Group
from accounts.models import Room


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST["email"]
        password = request.POST["psw"]
        username = request.POST["username"]

        user = auth.authenticate(
            email=email, password=password, username=username)
        if user is not None:
            auth.login(request, user)
            return redirect("/profile/username="+user.username)
        else:
            return redirect('/signup.html/')


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["psw"]
        password2 = request.POST["psw-repeat"]
        if password1 == password2:
            user = User.objects.create_user(
                email=email, password=password1, first_name=first_name, last_name=last_name, username=username)
            user.save()
            return render(request, "login.html")
        else:
            return render(request, "signup.html")
    else:
        return render(request, "signup.html")


def profile(request, username):
    return render(request, "profile.html")


def checkview(request):
    # if request.method == "GET":
    #     return render(request, "call_room.html")
    # else:
    room = request.POST['room_name']

    if Group.objects.filter(name=room).exists():
        return redirect("/call/")
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/')


def call(request):
    if request.method == "GET":
        return render(request, "call.html")
    else:
        q = request.POST['search']
        if q == "":
            return render(request, "call.html")
        else:
            posts = User.objects.filter(username__contains=q)
            return render(request, 'call.html', {'peer': posts})


def room(request, room_name):
    return render(request, "call_room.html")


def logout(request):
    auth.logout(request)
    return redirect("login/")
