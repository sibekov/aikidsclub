from django.shortcuts import render
from django.http import httpResponse
# Create your views here.
def index(render):
    return httpResponse("I will put my template here")