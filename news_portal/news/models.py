from django.db import models

# Create your models here.
class Samachar(models.Model):
    NEWS_CATEGORY = (
        ('P','Politics'),
        ('S','Sports'),
        ('H','Health'),
        ('B','Business'),
        ('E','Environment'),
        ('O','Others'),
        ('T','Technology'),
        ('R','Random'),
    )
    title=models.CharField(max_length=200,default='')
    image_link=models.CharField(max_length=200,default='')
    news_link=models.CharField(max_length=200,default='')
    news_category = models.CharField(max_length=1,choices=NEWS_CATEGORY,default='')


    def __str__(self):
        return self.title




  
    