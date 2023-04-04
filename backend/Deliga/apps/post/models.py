from django.db import models
from apps.account.models import User
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to = 'media/images/post')
    caption = models.CharField(max_length=300,blank=True,null=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=7,null=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=7,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    
    # def __str__(self):
    #     return self.caption
    

