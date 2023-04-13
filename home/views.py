from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request=request, template_name='home/welcome.html', context={'today': datetime.today()})


@login_required(login_url='/admin')
def secret(request):
    return render(request=request, template_name='home/secret.html')
