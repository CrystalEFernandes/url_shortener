from django.urls import path
from . import views

urlpatterns=[
    path('shorten/',views.shorten_url,name='shorten_url'),
    path('<str:alias>/',views.redirect_to_long_url,name='redirect_to_long_url'),
    path('analytics/<str:alias>/',views.get_analytics,name='get_analytics'),
    path('update/<str:alias>/',views.update_url,name='update_url'),
    path('delete/<str:alias>/',views.delete_url,name='delete_url'),
]