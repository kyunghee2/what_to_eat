from django.contrib import admin
from .models import Restaurant, Comment


class RestaurantAdmin(admin.ModelAdmin):

     list_display = ('pk','name','r_type','main_menu','img_path','people')


class CommentAdmin(admin.ModelAdmin):
     list_display = ('pk','restaurant', 'user', 'score', 'content', 'created_at', 'updated_at')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Comment, CommentAdmin)


# class Comment(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     score = models.FloatField(null=True, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

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