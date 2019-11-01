from django.urls import path

from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('<int:blog_id>',views.blog_detail,name='blog_detail'),
    path('<int:adds>/<int:added>',views.my_add,name='my_add'),
]