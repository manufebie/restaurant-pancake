from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.cart_detail, name='detail'),   
    url(r'^add/(?P<id>\d+)/$', views.add_menu_item, name='add'),
    url(r'^remove/(?P<id>\d+)/$', views.remove_menu_item, name='remove'),
]