from django.shortcuts import render, get_object_or_404
from .models import Restaurant
# import csv


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.order_by('?')[0:3]
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant/index.html', context )

def search(request):
    search = request.GET.get('search')
    restaurants = set(Restaurant.objects.filter(name__icontains=search))
    restaurants = set(Restaurant.objects.filter(name__icontains=search))
    restaurants.update(set(Restaurant.objects.filter(r_type__icontains=search)))
    restaurants.update(set(Restaurant.objects.filter(addr__icontains=search)))
    restaurants.update(set(Restaurant.objects.filter(main_menu__icontains=search)))

    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant/search.html', context)

def detail(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    temp = restaurant.content.split(",")
    temp2 = list()
    menu = list()
    for t in temp:
        temp2.append(t.strip())
    
    for t in temp2:
        item = list()
        item.append(t[:t.find("(")])
        item.append((t[t.find("(")+1:t.find(")")])+"원")
        menu.append(item)

    context = {
        'restaurant': restaurant,
        'menu': menu
    }
    return render(request, 'restaurant/detail.html', context)


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