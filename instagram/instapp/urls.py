
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),

    #home/12/
    url(r'^(?P<image_id>[0-9]+)/$',views.detail ,name='detail'),

]
