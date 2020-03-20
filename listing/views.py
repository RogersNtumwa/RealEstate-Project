from django.shortcuts import render
from .models import listing
# Create your views here.


def index(request):
    listings = listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listing/listings.html', context)


def singlelisting(request, listing_id):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
