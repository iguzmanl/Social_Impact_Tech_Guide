from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def homePageView(request):
    return render(request,'index.html')
    
def aboutPageView(request):
    return render(request,'about.html')

def guideView(request):
    return render(request,'guide_base.html')

def guideOverviewView(request):
    return render(request,'guide_overview.html')    