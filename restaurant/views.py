from django.shortcuts import render, redirect, get_object_or_404
from itertools import chain
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Restaurant, Comment
from .forms import CommentForm
import datetime
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

    comments = Comment.objects.filter(restaurant=restaurant)
    
    context = {
        'restaurant':restaurant,
        'menu': menu,
        'comments': comments,
        'month': datetime.datetime.today().month,
        'day': datetime.datetime.today().day
    }    
    return render(request, 'restaurant/detail.html',context)


@require_POST
def comments_create(request, restaurant_pk):
    restaurant = get_object_or_404(Restaurant, pk = restaurant_pk)
    if request.user.is_authenticated:
        comment = Comment.objects.create(restaurant=restaurant, score=request.POST['rating'], content=request.POST['commentText'],user=request.user)
        
    return redirect('restaurant:detail', restaurant_pk)

def chatbot_how_to_use (request):
    return render(request, 'restaurant/chatbot_how_to_use.html')

def people(request, people):
    restaurants = Restaurant.objects.filter(people=people)
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurant/search.html', context)

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


