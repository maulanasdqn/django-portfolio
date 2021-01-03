from django.shortcuts import render
from .models import Data

def index(request):
    data = Data.objects.all()
    g = {'data':data}
    return render(request, 'Frontend/index.html',g)
