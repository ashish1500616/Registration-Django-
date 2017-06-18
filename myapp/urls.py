from django.conf.urls import url

from . import views

app_name='myapp'

urlpatterns = [
    # url(r'^login/',views.login,name="login")
    url(r'^connect/', views.connect,name="conn"),
    url(r'^login/', views.login, name="login"),
    url(r'^user/', views.show_user,name="showuser"),
    url(r'^forms/',views.show_form,name="showform"),
    url(r'^form_page/',views.show_basic_form,name="showbasicform"),
]
