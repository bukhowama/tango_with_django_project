from django.conf.urls import url
from rango import views

urlpatterns = [
        url(r'^$', views.index, name='index'),

        url(r'^index/', views.index, name='index'),
        #is this correct??

        url(r'^about/', views.about, name='about'),
]


