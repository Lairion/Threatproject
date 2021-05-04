from django.shortcuts import render, redirect
from case.models import Case
from case.task import (repeat_case)
# Create your views here.
def home(request):
    all_case = Case.objects.all()
    return render(request, 'case/case.html', {'cases': all_case})

def make_repeat(request):
    if request.method == "POST":
        for i in dict(request.POST)["cases"]:
            repeat_case.delay(int(i), int(request.POST.get("repeat")))
    return redirect("home")
    
