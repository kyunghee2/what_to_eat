from django.db import models
from django.conf import settings

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    r_type = models.CharField(max_length=4)
    addr = models.CharField(max_length=400,null=True, blank=True)
    r_lati = models.FloatField(null=True, blank=True)
    r_long = models.FloatField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    main_menu = models.CharField(max_length=200)
    img_path = models.ImageField(blank=True)
    people = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.name}'

class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk',] 

    def __str__(self):
        return self.content