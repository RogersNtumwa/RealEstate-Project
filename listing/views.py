from django.shortcuts import render
from .models import listing
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.shortcuts import get_object_or_404
from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listing/listings.html', context)


def singlelisting(request, listing_id):
    get_listing = get_object_or_404(listing, pk=listing_id)

    context = {
        'get_listing': get_listing
    }
    return render(request, 'listing/listing.html', context)


def search(request):
    context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'listing/search.html', context)
