from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    body = models.TextField(max_length=2250)
    published = models.DateField(default=datetime.now())

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
        # return self.pk
    
    