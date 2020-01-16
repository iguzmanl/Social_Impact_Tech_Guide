from django.urls import path

from .views import homePageView,aboutPageView,guideView,guideOverviewView,guideEventView

urlpatterns = [
    path('', homePageView, name='home'),
    path('/about', aboutPageView, name='about'),
    path('/guide', guideView, name='guide'),
    path('/guide/overview', guideOverviewView, name='guideoverview'),
    path('/guide/guideevents', guideEventView, name='guideEvents'),
    
]