from django.urls import path

from .views import homePageView,aboutPageView,guideView,guideTopics,guideOverviewView,guideEventView, jobAppView, guideReccomendationsView, contactPageView

from . import views

urlpatterns = [
    path('', homePageView, name='home'),
    path('/about', aboutPageView, name='about'),
    path('/contact', contactPageView, name='contact'),
    path('/guide', guideView, name='guide'),
    path('/guide/overview', guideOverviewView, name='guideoverview'),
    path('/guide/topics', guideTopics, name='guidetopics'),
    path('/guide/reccomendations', guideReccomendationsView, name='reccomendations'),
    path('/guide/guideevents', guideEventView, name='guideEvents'),
    path('/job_app', views.jobAppView, name = 'job_app')
    # path('', views.home, name='home'),
]
