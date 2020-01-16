from django.urls import path

<<<<<<< HEAD
from .views import homePageView,aboutPageView,guideView,guideTopics,guideOverviewView,guideEventView, jobAppView, guideReccomendationsView, contactPageView
=======
from .views import homePageView,aboutPageView,guideView,guideOverviewView,guideEventView, jobAppView, guideReccomendationsView, contactPageView, guideProjects, guideFields
>>>>>>> 6ea846bbc2a53e5d98fab2cf31c5313cea0fb602

from . import views

urlpatterns = [
    path('', homePageView, name='home'),
    path('/about', aboutPageView, name='about'),
    path('/contact', contactPageView, name='contact'),
    path('/guide', guideView, name='guide'),
    path('/guide/overview', guideOverviewView, name='guideoverview'),
<<<<<<< HEAD
    path('/guide/topics', guideTopics, name='guidetopics'),
=======
    path('/guide/fields', guideFields, name='guidefields'),
    path('/guide/projects', guideProjects, name='guideprojects'),
>>>>>>> 6ea846bbc2a53e5d98fab2cf31c5313cea0fb602
    path('/guide/reccomendations', guideReccomendationsView, name='reccomendations'),
    path('/guide/guideevents', guideEventView, name='guideEvents'),
    path('/job_app', views.jobAppView, name = 'job_app')
    # path('', views.home, name='home'),
]
