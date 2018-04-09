from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.create_order, name='create'),
    url(r'^list/$', views.OrderListView.as_view(), name='list'),
]