from django.shortcuts import render
from .models import Restaurant
# import csv


# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html' )

def query(request):
    query = request.GET.get('query')
    restaurants = set(Restaurant.objects.filter(name__icontains=query))
    restaurants.update(set(Restaurant.objects.filter(r_type__icontains=query)))
    restaurants.update(set(Restaurant.objects.filter(addr__icontains=query)))
    restaurants.update(set(Restaurant.objects.filter(main_menu__icontains=query)))
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant/query.html', context)

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