from django.conf.urls import url
from . import views
app_name='mywebsite'
urlpatterns = [
url(r'^$',views.logininput, name='logininput'),
url(r'^reginput$',views.reginput,name='reginput'),
url(r'^login$',views.login,name='login'),
url(r'^reg$',views.reg,name='reg'),

]