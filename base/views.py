from django.shortcuts import render
from .models import Linklist

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        college = request.POST['college']
        print(name,college)

        newList = Linklist.objects.create(name=name,college=college)

    allList = Linklist.objects.all()
    contaxt = {'allList':allList}
    return render(request, 'home.html',contaxt)
