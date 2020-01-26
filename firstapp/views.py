from django.shortcuts import render
# Create your views here.

from .decorators import decorator1

from django.http import HttpResponse

@decorator1
def demo(request,value):

    return "TEST"

def home(request):

    # ex = 3/0
    print(demo(request,3))
    # print(request.GET)

    return HttpResponse("Exception")

def template_test(request):


    return render(request,'test.html')