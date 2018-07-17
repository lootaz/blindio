from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator

from blindio_common.decorators import login_required
from blindio_common.views import CommonView


class SettingsView(CommonView):
    template_name = "blindio_settings/settings.html"

    def get_all_settings(self):
        settings = [
            {"name": "setting.pacs", "label": "PACS", "href": reverse('blindio_settings:pacs_settings'),
             "template_name": "blindio_settings/pacs_settings.html"},
            {"name": "setting.video", "label": "Video", "href": reverse('blindio_settings:video_settings'),
             "template_name": "blindio_settings/video_settings.html"},
            {"name": "setting.hospital", "label": "Hospital", "href": reverse('blindio_settings:hospital_settings'),
             "template_name": "blindio_settings/hospital_settings.html"},
        ]

        return settings

    @method_decorator(login_required)
    def get(self, request, setting_name=None):
        self.prepare_top_menu("blindio_settings.settings")
        all_settings = self.get_all_settings()

        context_settings = []
        for setting in all_settings:
            context_setting = {
                "active": False,
                "label": setting.get("label", ""),
                "href": setting.get("href", ""),
                "template_name": setting.get("template_name", ""),
            }
            if (not setting_name is None) and (setting.get("name") == setting_name):
                context_setting["active"] = True

            context_settings.append(context_setting)
        if setting_name is None:
            context_settings[0]["active"] = True

        self.context["settings"] = context_settings
        return render(request, self.template_name, self.context)
