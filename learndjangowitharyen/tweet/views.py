from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'index.html') # "Find the template file index.html, render it, and return it as an HTML response to the user."

