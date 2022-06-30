from distutils.command.upload import upload
from email.policy import default
from tarfile import BLOCKSIZE
from xml.etree.ElementTree import Comment
from django.db import models


class Comment(models.Model):
    comment=models.TextField(null=True)
    commentdate=models.DateField(auto_now=True)



class Download(models.Model):
    pass


class Like(models.Model):
    likedate=models.DateField(auto_now=True)
    pass
    


# Create your models here.
class  Item(models.Model):
    name=models.CharField(max_length=87,null=True)
    description=models.TextField(null=True)
    shortdescription=models.CharField(default="this is a short description " ,max_length=100)
    type=models.CharField(default="game",max_length=120)
    uploaddate=models.DateField(auto_now=True)


    file=models.FileField(upload_to="storefile")
    icon=models.FileField(upload_to="storeitemicon")
    overview=models.FileField(upload_to="overviewitem",blank=True)

    makepub=models.BooleanField(default=False)
    onlinepricing=models.FloatField(default=0)
    allowdownload=models.BooleanField(default=True)
    Downloadpricing=models.FloatField(default=0)


    visibility=models.CharField(default="public",max_length=100)


    presentation=models.FileField(upload_to="presentation")
    
def __str__(self) -> str:
    return self.name




