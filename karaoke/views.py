from django.shortcuts import render
from django.http import HttpResponse
from karaoke.populate_from_csv import populate_db
# Create your views here.


def populate(request):
	populate_db()
	return HttpResponse("It's been populated!")