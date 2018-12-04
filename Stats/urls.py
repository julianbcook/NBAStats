from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^i', views.index, name='index'),
               url(r'^l', views.login, name = 'login'),
               url(r'^c',views.charts, name = 'charts'),
               url(r'^t',views.tables, name = 'tables'),
               url(r'^r',views.register, name = 'register'),
               url(r'^f',views.forgot, name = 'forgotPassword'),
               url(r'^4',views.badPage, name = '404Page'),
               url(r'^b',views.blank, name = 'blank'),
               url(r'^tt', views.teamtables, name = 'teamtables'),
]
