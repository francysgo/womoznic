from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.base, name='base'),
    url(r'^$', views.base),
    url(r'^$', views.inicio),
    url(r'', include('blog.urls')),


]
