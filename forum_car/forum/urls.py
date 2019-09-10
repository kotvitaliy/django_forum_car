from django.conf.urls import url
from . import views, auth_views
from django.urls import path

app_name = 'forum'

urlpatterns = [
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),
    path('login', auth_views.login_, name='login'),
    path('register', auth_views.register_, name='register'),
    path('logout', auth_views.logout_, name='logout'),
    path('', views.index, name='index'),
    path('cabinet', views.cabinet, name='cabinet'),



]


