from django.conf.urls import url

from . import views

app_name = 'blindio_monitor'
urlpatterns = [
    url(r'^studies_state/$', views.StudiesStateView.as_view(), name='studies_state'),
    url(r'^system_state/$', views.SystemStateView.as_view(), name='system_state'),
]
