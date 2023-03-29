from django.db import models
from django.contrib.auth.models import AbstractUser, User
import os
from uuid import uuid4
from PIL import Image


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    twitter_profile = models.TextField()
    facebook_profile = models.TextField()
    instagram_profile = models.TextField()
    linkedin_profile = models.TextField()
    user_image = models.ImageField(upload_to=path_and_rename, default="")


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to=path_and_rename, default="")
    category = models.TextField(default="10")

