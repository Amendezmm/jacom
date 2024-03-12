from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def masterpage(request):
    tpt = loader.get_template("master.html") 
    context = {
        "titulo":"Pagima principal",
        "building": "Sitio en Construcción",

    }
    return HttpResponse(tpt.render(context, request))
