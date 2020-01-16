from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import JobListing

def homePageView(request):
    return render(request,'index.html')

def aboutPageView(request):
    return render(request,'about.html')

def contactPageView(request):
    return render(request,'contact.html')

def guideView(request):
    return render(request,'guide_base.html')


def guideOverviewView(request):
    return render(request,'guide_overview.html', {'overview':'active', 'tech_fields': '', 'tech_projects':'', 'events':'', 'recs':''})

def guideFields(request):
    return render(request,'guide_fields.html', {'overview':'', 'tech_fields': 'active', 'tech_projects':'', 'events':'', 'recs':''})
def guideProjects(request):
    return render(request,'guide_projects.html', {'overview':'', 'tech_fields': '', 'tech_projects':'active', 'events':'', 'recs':''})

def guideEventView(request):
    import config
    from airtable import airtable
    at = airtable.Airtable(config.at['base_id'], config.at['api_key'])
    table = at.get('Social Impact Conference')
    records = table['records']
    eventList = []
    for r in records:
        eventList.append(r['fields'])
        print(r)
    print("used config!")
    return render(request,'guide_events.html',{'event_list': eventList, 'overview':'', 'tech_fields': '', 'tech_projects':'', 'events':'active', 'recs':''})

def guideReccomendationsView(request):
    import config
    from airtable import airtable
    at = airtable.Airtable(config.at['base_id'], config.at['api_key'])
    table = at.get('Our Reccomendations')
    records = table['records']
    eventList = []
    for r in records:
        eventList.append(r['fields'])
        print(r)
    print("used config!")
    return render(request,'guide_reccomendations.html',{'reccomendations': eventList, 'overview':'', 'tech_fields': '', 'tech_projects':'', 'events':'', 'recs':'active'})

def jobAppView(request):
    job_listings = JobListing.objects.all()
    context = {'job_listings': job_listings}

    if request.method == "POST":

        posted_title = request.POST.get("title", "")
        posted_OppType = request.POST.get("OppType", "")
        posted_eligibility = request.POST.get("eligibility", "")
        posted_appDueDate = request.POST.get("appDueDate", "")
        posted_oppDates = request.POST.get("oppDates", "")
        posted_description = request.POST.get("description", "")
        posted_location = request.POST.get("location", "")
        posted_link_external = request.POST.get("link_external", "")


        # print(title *100)
        # print(description *100)

        job_listing = JobListing.objects.create(
            title = posted_title,
            description = posted_description,
            OppType = posted_OppType,
            eligibility = posted_eligibility,
            appDueDate = posted_appDueDate,
            oppDates = posted_oppDates,
            location = posted_location,
            link_external = posted_link_external
        )
        job_listing.save()

        return render(request, "jobs_app/index.html", context)


    return render(request, "jobs_app/index.html", context)
