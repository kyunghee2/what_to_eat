from django.shortcuts import render
from .models import Restaurant
# import csv


# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html' )

def search(request):
    search = request.GET.get('search')
    restaurants = Restaurant.objects.filter(name__icontains=search)
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant/search.html', context)

# def detail(request, restaurant_pk):

#     pass

def detail(request):
    return render(request, 'restaurant/detail.html')

# def csvfilesave(request):
#     with open('whattoeat_db.csv', newline='', encoding='UTF8') as csvfile:
#         reader = csv.DictReader(csvfile)

#         for row in reader:
#             #print('>>>>>')
#             #print(row)
#             name = row['\ufeffname']
#             r_type = row['r_type']
#             main_menu= row['main_menu']
#             addr=row['addr']
#             content=row['content']

#             rest = Restaurant(name=name,r_type=r_type,main_menu=main_menu,addr=addr,content=content)
#             rest.save()

#     return render(request,'restaurant/index.html') 