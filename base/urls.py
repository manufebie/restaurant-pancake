from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views # Django authentication system
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # Auth views
    url(r'^$', auth_views.LoginView.as_view(template_name='index.html'), 
        name='home'), # Home page/Login page
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), # Logout
    # App include urls
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^menu/', include('menu.urls', namespace='menu')),
    url(r'^order/', include('orders.urls', namespace='order'))
]

# Static configs for development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
