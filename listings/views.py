from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing
from .choices import price_choices, state_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html',context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing' : listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):

    context = {
        'price_choices' : price_choices,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
    }

    return render(request, 'listings/search.html', context)
