from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^login/',views.login,name="login")
    url(r'^connect/', views.connect,),
    url(r'^login/', views.login, name="login"),
    url(r'^user/', views.show_user,name="showuser"),

]
