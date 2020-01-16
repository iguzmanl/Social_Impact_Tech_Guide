from django.shortcuts import render
from .models import JobListing
# Create your views here.

def home(request):
    job_listings = JobListing.objects.all()
    context = {'job_listings': job_listings}

    if request.method == "POST":

        posted_title = request.POST.get("title", "")
        posted_OppType = request.POST.get("OppType", "")
        posted_eligibility = request.POST.get("title", "")
        posted_appDueDate = request.POST.get("description", "")
        posted_oppDates = request.POST.get("OppType", "")
        posted_description = request.POST.get("description", "")
        posted_location = request.POST.get("title", "")
        posted_link_external = request.POST.get("OppType", "")

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
