from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# it's a request handler
#request -> response

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Debaraj'})