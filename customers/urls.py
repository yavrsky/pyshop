from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.best_customers, name='best_customers'),
]