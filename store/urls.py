from django.urls import path
from . import views 
urlpatterns = [
    path('app/',views.Appview.as_view(),name="store"),
         path('app/<id>',views.Itemprogramview.as_view(),name="storeitemprogram"),
     path('',views.Storehomeview.as_view(),name="storehome"),
]
