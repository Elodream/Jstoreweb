from operator import itemgetter
from urllib.request import Request
from django.shortcuts import render
from django.views import View
from .models import  Item


class Storehomeview(View):
   template="storebase.html"
   def get(self,request,*args,**kwargs):
      games=Item.objects.filter(type="game")
      apps=Item.objects.filter(type="application")
      packages=Item.objects.filter(type="package")
      url="store"
      return render(request,self.template,context={"packages":packages,"apps":apps,"games":games})


class Appview(View):
   template="app.html"
   def get(self,request,*args,**kwargs):
      apps=Item.objects.filter(type="application")
      url="store"
      return render(request,self.template,context={"apps":apps})


class packageview(View):
   template="app.html"
   def get(self,request,*args,**kwargs):
      packages=Item.objects.filter(type="packages")
      url="store"
      return render(request,self.template,context={"packages":packages})


class Gameview(View):
   template="app.html"
   def get(self,request,*args,**kwargs):
     
      games=Item.objects.filter(type="game")
      url="store"
      return render(request,self.template,context={"games":games})


class Itemprogramview(View):
   template="itemprogram.html"
   def get(self,request,*args,**kwargs):
      pk=kwargs['id']
      itemprogram=Item.objects.get(pk=pk)
      fileurl="http://"+request.get_host()+itemprogram.file.url
      url="store"
      return render(request,self.template,context={"item":itemprogram,"file":fileurl})


class Itempackageview(View):
   template="itempackage.html"
   def get(self,request,*args,**kwargs):
      games=Item.objects.filter(type="game")
      url="store"
      return render(request,self.template,context={"games":games})

class Itemmediaview(View):
   template="itemmedia.html"
   def get(self,request,*args,**kwargs):
      games=Item.objects.filter(type="game")
      url="store"
      return render(request,self.template,context={"games":games})