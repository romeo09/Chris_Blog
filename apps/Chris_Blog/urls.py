from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'main_page'),
    url(r'^blogs$', views.blogs, name = 'blogs'),
    url(r'^comments$',views.comments, name = 'comments'),
]
