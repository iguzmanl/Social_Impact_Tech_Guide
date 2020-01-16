from django.db import models

# Create your models here.
from django.db.models import (
    Model,
    TextField
)

# Create your models here.
class JobListing(Model):
    title = TextField(null = True, blank = True)
    OppType = TextField(null = True, blank = True)
    eligibility = TextField(null = True, blank = True)
    appDueDate = TextField(null = True, blank = True)
    oppDates = TextField(null = True, blank =True)
    description = TextField(null = True, blank =True)
    location = TextField(null = True, blank = True)
    link_external = TextField(null = True, blank =True)
