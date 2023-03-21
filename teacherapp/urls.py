from django.urls import path

from teacherapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view'),
]