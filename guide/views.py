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
def guideEventView(request):
    import config
    from airtable import airtable
    at = airtable.Airtable(config.at['base_id'], config.at['api_key'])
    table = at.get('Social Impact Conference')
    records = table['records']
    eventList = []
    for r in records:
        eventList.append(r['fields'])
    print("used config!")
    return render(request,'guide_events.html',{'events': eventList})    