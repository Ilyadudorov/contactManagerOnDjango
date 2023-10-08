from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', indexMain),
    path('weather/', index, name='home'),
    # path('cats/<int:catid>', categories),
    re_path('cats/(\d{1,3})', categories)
    
]


 
 

