from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *

# Create your views here.


def index(req):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(req, 'ajax_app/index.html', context)


def snakeForm(req):
    return render(req, 'ajax_app/snakeform.html')


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
    return redirect(f"/getsnake/{newSnake.id}")


def newlyadded(req, id):
    context = {
        'snake': Snake.objects.get(id=id)
    }
    return render(req, 'ajax_app/newsnake.html', context)


def allsnakes(req):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(req, "ajax_app/allsnakes.html", context)


def deleteSnake(req, id):
    Snake.objects.get(id=id).delete()
    return redirect("/allsnakes")
