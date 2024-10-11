from django.urls import path
from .views import Base, Barnview
urlpatterns = [
    
    path('', Base.as_view(), name='base'),
    path('barn/', Barnview.as_view(), name='barn'),
]
