from django.conf.urls import url
from django.contrib import admin
from elasticsearchapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.search, name='search'), # < here
]
