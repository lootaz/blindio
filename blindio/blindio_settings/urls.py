from django.conf.urls import url

from . import views
from . import api

app_name = 'blindio_settings'
urlpatterns = [
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
    url(r'^settings/pacs/$', views.SettingsView.as_view(), {"setting_name": "setting.pacs"}, name='pacs_settings'),
    url(r'^settings/video/$', views.SettingsView.as_view(), {"setting_name": "setting.video"}, name='video_settings'),
    url(r'^settings/hospital/$', views.SettingsView.as_view(), {"setting_name": "setting.hospital"},
        name='hospital_settings'),
    url(r'^settings/(?P<name>[A-Za-z0-9_-]+)/$', api.SettingApi.as_view(), name='setting_api'),
]
