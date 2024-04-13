from django.shortcuts import render, httpResponse
# Create your views here.
def index(render):
    return httpResponse("I will put my template here")