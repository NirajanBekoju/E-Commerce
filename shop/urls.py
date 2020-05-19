from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('contact', views.contact),
    path('tracker', views.tracker),
    path('search', views.search),
    path('product/<int:proId>', views.productView),
    path('checkout', views.checkout),
]
