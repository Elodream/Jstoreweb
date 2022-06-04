from operator import itemgetter
from django.shortcuts import render
from django.views import View
from .models import  Item

class Appview(View):
   template="app.html"
   def get(self,request,*args,**kwargs):
        games=Item.objects.filter(type="game")
        apps=Item.objects.filter(type="application")
        films=Item.objects.filter(type="film")
        url="store"
        return render(request,self.template,context={"films":films,"apps":apps,"games":games})
