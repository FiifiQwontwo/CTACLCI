from django.shortcuts import render, get_object_or_404
from ctac.models import *
from django.db.models import Q


# Create your views here.
def search(request):
    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':
            query = 'results'

        results = Member.objects.filter(
            Q(surname__icontains=query) | Q(first_name__icontains=query) | Q(second_name__icontains=query))

    return render(request, 'search.html', {'query': query, 'results': results})
