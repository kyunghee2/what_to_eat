from django.shortcuts import render
import csv
from .models import Restaurant
# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html' )