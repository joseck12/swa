from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    """ The home page"""
    details = AboutChurch.objects.all()
    return render(request, 'swapp/home.html', {'details': details})


def about(request):
    """The about page for swa."""
    details = AboutChurch.objects.all()

    return render(request, 'swapp/about.html', {'details': details})


def pastors(request):
    """About the Bishop of SWA"""
    bio = PastorsProfile.objects.all()
    details = AboutChurch.objects.all()

    return render(request, 'swapp/pastors.html', {'bio': bio}, {'details': details})


def services(request):
    """The available church services"""
    programs = ChurchServices.objects.all()
    details = AboutChurch.objects.all()

    return render(request, 'swapp/services.html', {'programs': programs}, {'details': details})


def projects(request):
    """Ongoing projects"""
    project = Project.objects.all()
    details = AboutChurch.objects.all()

    return render(request, 'swapp/projects.html', {'project': project}, {'details': details})


def events(request):
    """Upcoming events"""
    activities = Event.objects.all()
    details = AboutChurch.objects.all()

    return render(request, 'swapp/events.html', {'activities': activities}, {'details': details})

def givings(request):
    """Contribution details"""
    contribution = Giving.objects.all()

    return render(request, 'swapp/giving.html', {'contribution': contribution})

def blog(request):
    """Blog section"""
    return render(request, 'swapp/blog.html')

def contact(request):
    """The contacts page for swapp."""
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()
    details = AboutChurch.objects.all()
    return render(request, 'swapp/contact.html', {'details': details})
