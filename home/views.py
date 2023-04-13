from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def home(request):
    return render(request=request, template_name='home/welcome.html', context={'today': datetime.today()})
