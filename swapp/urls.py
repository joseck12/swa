"""Defines URL patterns for swapp."""

from django.urls import path
from . import views

app_name = 'swapp'
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # About Page
    path('about/', views.about, name='about'),
    # Page for the bishop's profile
    path('pastors/', views.pastors, name='pastors'),
    # A page for the church services
    path('services/', views.services, name='services'),
    # A page for church projects
    path('projects/', views.projects, name='projects'),
    # A page for upcoming church activities
    path('events/', views.events, name='events'),
    # Contributions Page
    path('giving/', views.givings, name='givings'),
    # Blog Page
    path('blog/', views.blog, name='blog'),
    # Contact details page
    path('contact/', views.contact, name='contact'),
]
