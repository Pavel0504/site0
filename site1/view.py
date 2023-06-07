from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):

    # return render(request, "index.html", {'uname':request.META['REMOTE_USER']} )
    return render(request, "index.html", {'uname': os.environ.get('USER')} )
