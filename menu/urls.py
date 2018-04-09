from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.MenuItemListView.as_view(), name='list')
    url(r'^$', views.menu_list, name='list'),
    url(r'^(?P<id>\d+)/$', views.menu_item_detail, name='detail'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.menu_list, name='category-list'),
]