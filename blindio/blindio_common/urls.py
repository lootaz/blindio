from django.conf.urls import url

from . import views

app_name = 'blindio_common'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^login/S', views.LoginView.as_view(), name="login"),
    url(r'^logout/S', views.LogoutView.as_view(), name="logout"),
]
