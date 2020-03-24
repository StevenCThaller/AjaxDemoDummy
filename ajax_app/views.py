from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *

# Create your views here.


def index(req):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(req, 'index.html', context)


def snakeForm(req):
    return render(req, 'snakeform.html')


def addSnake(req):
    if('venomous' in req.POST):
        ven = True
    else:
        ven = False
    errors = Snake.objects.snake_validate(req.POST)
    if len(errors) > 0:
        for tags, value in errors.items():
            messages.error(req, value, extra_tags=tags)
        error = {error: 403}
        return JsonResponse(error)
    newSnake = Snake.objects.create(
        name=req.POST['name'], length=req.POST['length'], venomous=ven)
    return redirect(f"/snakes/{newSnake.id}")


def oneSnake(req, snake_id):
    context = {
        'snake': Snake.objects.get(id=snake_id)
    }
    return render(req, 'newsnake.html', context)


def allSnakes(req):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(req, "allsnakes.html", context)


def deleteSnake(req, snake_id):
    Snake.objects.get(id=snake_id).delete()
    return redirect("/snakes/all")
