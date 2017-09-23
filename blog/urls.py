from django.conf.urls import url
from . import views  #importo tutte le viste una volta sola dalla cartella corrente (.)

urlpatterns =[
	url(r'^$', views.post_list, name = 'post_list'),
]