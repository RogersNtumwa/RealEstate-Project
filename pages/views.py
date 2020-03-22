from django.shortcuts import render
from listing.models import listing
from realtor.models import realtor
from listing.choices import price_choices, bedroom_choices, state_choices
# Create your views here.


def index(request):
    listings = listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,

    }
    return render(request, 'pages/index.html', context)


def about(request):
    Realtors = realtor.objects.order_by('-hire_date')
    mvp_realtor = realtor.objects.all().filter(is_mvp=True)
    context = {
        "Realtors": Realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
