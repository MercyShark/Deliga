from django.db import models
from apps.account.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    bio = models.CharField(max_length=200,null=True)
    avatar = models.ImageField(upload_to="media/images/userprofile/avatar",null=True)
    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username