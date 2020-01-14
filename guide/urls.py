from django.urls import path

from .views import homePageView,aboutPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('/about', aboutPageView, name='about'),
]