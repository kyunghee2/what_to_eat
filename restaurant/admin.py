from django.contrib import admin
from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):

     list_display = ('pk','name','r_type','main_menu','img_path','people')





admin.site.register(Restaurant, RestaurantAdmin)

    # name = models.CharField(max_length=200)
    # r_type = models.CharField(max_length=4)
    # addr = models.CharField(max_length=400,null=True, blank=True)
    # r_lati = models.FloatField(null=True, blank=True)
    # r_long = models.FloatField(null=True, blank=True)
    # content = models.TextField(null=True, blank=True)
    # main_menu = models.CharField(max_length=200)
    # img_path = models.ImageField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)