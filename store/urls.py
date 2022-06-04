from django.urls import path
from . import views 
urlpatterns = [
    path('/app/',views.Appview.as_view()),
     path('',views.Appview.as_view()),
]
