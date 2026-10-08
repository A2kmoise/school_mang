from .views import greetings, greetings2, greetings3
from django.urls import path

urlpatterns = [
    path('greetingmoise/', greetings, name='greetings'),
    path('greetingsbenise/', greetings2, name='greetings2'),
    path('greetingsdelice/', greetings3, name='greetings3'),
]
