from django.shortcuts import render, get_object_or_404

from properties.models import Property, Picture


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
