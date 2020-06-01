from .views import homeview,aboutview,portfolioview,priceview,servicesview,contactview
from django.urls import path
app_name = 'home'


urlpatterns = [
    path('', homeview,name='home'),
    path('about',aboutview,name='about'),
    path('portfolio',portfolioview,name = 'portfolio'),
    path('price',priceview,name = 'price'),
    path('service',servicesview,name = 'service'),
    path('contact',contactview,name = 'contact'),


]
