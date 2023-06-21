from django.conf.urls import url
from .views import archive, create_blogpost


urlpatterns = [
    url(r'^$', archive),
    url(r'^create/$', create_blogpost),
]
