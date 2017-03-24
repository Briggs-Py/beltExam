from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..loginAndReg.models import User
from .models import Wishlist

def index(request, id):
    user = User.objects.get(id=id)
    context = {
        "wishlist": Wishlist.objects.filter(users=user),
        "othersWishlist": Wishlist.objects.exclude(users=user)
    }
    return render(request, "mainApp/index.html", context)

def new(request, id):
    return render(request, "mainApp/new.html")

def process(request, id):
    user = User.objects.get(id=id)

    if len(request.POST['name']) < 1:
        messages.add_message(request, messages.WARNING, "Name cannot be blank.")
        return redirect(reverse('main:new', kwargs={'id': user.id}))
    if len(request.POST['name']) < 3:
        messages.add_message(request, messages.WARNING, "Name must be at least three characters.")
        return redirect(reverse('main:new', kwargs={'id': user.id}))

    wish = Wishlist.objects.create(name=request.POST['name'], creator=user)
    wish.users.add(user)

    return redirect(reverse('main:index', kwargs={'id': user.id}))

def show(request, id):
    context = {
    "item": Wishlist.objects.get(id=id),
    "users":User.objects.filter(wishes__id=id)
    }
    return render(request, "mainApp/show.html", context)

def remove(request, id):
    user = User.objects.get(id=request.session['user'])
    wish = Wishlist.objects.get(id=id)
    wish.users.remove(user)
    return redirect(reverse('main:index', kwargs={'id': user.id}))

def add(request, id):
    user = User.objects.get(id=request.session['user'])
    wish = Wishlist.objects.get(id=id)
    wish.users.add(user)
    return redirect(reverse('main:index', kwargs={'id': user.id}))

def goback(request):
    return redirect(reverse('main:new'))

def delete(request, id):
    user = User.objects.get(id=request.session['user'])
    Wishlist.objects.get(id=id).delete()
    return redirect(reverse('main:index', kwargs={'id': user.id}))
