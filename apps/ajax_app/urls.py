from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addsnake$', views.addSnake),
    url(r'^allsnakes$', views.allsnakes),
    url(r'^snakeform$', views.snakeForm),
    url(r'^getsnake/(?P<id>\d+)$', views.newlyadded),
    url(r'^deletesnake/(?P<id>\d+)$', views.deleteSnake),
]
