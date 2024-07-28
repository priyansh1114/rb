from django.shortcuts import render
from django.http import HttpResponse
from .rabbitmq import publish_message

# Create your views here.
def index(request):
    publish_message("Hi this is msg")
    return HttpResponse("Messaged Pushed to rabbitMQ")