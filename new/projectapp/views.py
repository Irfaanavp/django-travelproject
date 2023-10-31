from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team



# Create your views here.
def index(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request, "index.html", {'result': obj,'result1':obj1})

# def result(request):
#   x=int(request.GET['value1'])
#   y=int(request.GET['value2'])
#   res=x+y
#    return render(request, "result.html",{'result':res})


# def newpage(request):
# return HttpResponse("django new page")
