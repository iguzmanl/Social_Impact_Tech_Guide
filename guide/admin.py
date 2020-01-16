from django.contrib import admin

# Register your models here.
from .models import JobListing
# from .models import FeedbackComments
# Register your models here.

class JobListingAdmin(admin.ModelAdmin):
    list_display = ['title','OppType','eligibility', 'appDueDate', 'oppDates', 'description', 'location','link_external' ]


# class FeedbackCommentsAdmin(admin.ModelAdmin):
#     list_display = ['name','email','message' ]

admin.site.register(JobListing, JobListingAdmin)
