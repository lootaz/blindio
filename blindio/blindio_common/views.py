from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from blindio_common.services import get_top_menu_items


class CommonView(View):
    def __init__(self):
        super(CommonView, self).__init__()
        self.context = {}

    def prepare_top_menu(self, active_menu_name=None):
        top_menu_items = get_top_menu_items()
        if not active_menu_name is None:
            for top_menu_item in top_menu_items:
                if top_menu_item.get("name") == active_menu_name:
                    top_menu_item["active"] = True
                    break

        self.context["top_menu_items"] = top_menu_items


class IndexView(CommonView):
    template_name = "blindio_common/index.html"

    def get(self, request):
        self.prepare_top_menu()
        alert_message = request.session.get("alert_message", None)
        if alert_message:
            self.context["alert_message"] = alert_message
            del request.session["alert_message"]
        return render(request, self.template_name, self.context)


class LoginView(View):
    redirect_field_name = REDIRECT_FIELD_NAME

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
        else:
            request.session["alert_message"] = {
                "class": "alert-danger",
                "content": "Wrong username or password",
                "hide_delay": 5000
            }
        return redirect('blindio_common:index')


class LogoutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('blindio_common:index')
