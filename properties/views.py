from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from properties.models import Property, Picture
from .models import Contact


def home(request):
    properties = Property.objects.all()
    return render(request, 'properties/home.html', {
        'properties': properties
    })


def detail(request, slug):
    property = Property.objects.get(slug=slug)
    images = Picture.objects.filter(property=property)
    return render(request, 'properties/detail.html', {
        'property': property,
        'images': images
    })


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)

    else:
        form = ContactForm()

    return render(request, 'properties/contact_us.html', {
        'form': form
    })


def about_us(request):
    return render(request, 'properties/about_us.html')


def services(request):
    return render(request, 'properties/services.html')
