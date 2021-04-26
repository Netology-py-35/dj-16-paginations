import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

rows = []


def index(request):
    return redirect(reverse(bus_stations))


def read_cvs(file_name):
    rows = []
    with open(file_name, 'r', encoding="cp1251") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def bus_stations(request):
    # current_page = 1
    # next_page_url = 'write your url'
    # # page_number = int(request.GET.get('page', 1))
    CONTENT = read_cvs('data-398-2018-08-30.csv')

    paginator = Paginator(CONTENT, 10)  # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'list': page_obj})

