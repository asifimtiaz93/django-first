from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request, *args,**kwargs):
    #return HttpResponse ("<h1>Hello to my little friend!!</h1>")
    return render (request,"home.html",{})


def contact (request, *args, **kwargs):
    #return HttpResponse("<h1> contact page</h1>")
    return render (request,"contact.html",{})

def about (request, *args, **kwargs):
    my_context={
        "my_text":"hello friend",
        "my_number":123,
        "my_list": [111,222,333]
    }
    return render (request,"about.html",my_context)
