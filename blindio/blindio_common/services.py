from django.urls import reverse


def get_top_menu_items():
    top_menu_items = [
        {"name": "blindio_monitor.system_state", "label": "System", "url": reverse("blindio_monitor:system_state")},
        {"name": "blindio_monitor.studies_state", "label": "Studies", "url": reverse("blindio_monitor:studies_state")},
        {"name": "blindio_settings.settings", "label": "Settings", "url": reverse("blindio_settings:settings")},
    ]

    return top_menu_items
