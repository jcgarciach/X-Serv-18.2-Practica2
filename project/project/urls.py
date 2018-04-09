
from django.conf.urls import include, url
from django.contrib import admin
from acorta_url import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.pag, name = "Página principal"),
    url(r'^(\d+)$', views.redir, name = "Redireccionar a la url")
]
