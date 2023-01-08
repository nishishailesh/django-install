from django.urls import path, include
import home.views, ma.urls, food.urls

urlpatterns = [
    path('authentication/', include("django.contrib.auth.urls")),      #this is a string. not required to import
    path('', home.views.index, name='home')  ,  
    path('ma/', include(ma.urls)),
    #path('food/', include(food.urls)),
]
