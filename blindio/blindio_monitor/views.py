from django.shortcuts import render
from django.utils.decorators import method_decorator

from blindio_common.decorators import login_required
from blindio_common.views import CommonView


class StudiesStateView(CommonView):
    template_name = "blindio_monitor/studies_state.html"

    @method_decorator(login_required)
    def get(self, request):
        self.prepare_top_menu("blindio_monitor.studies_state")
        return render(request, self.template_name, self.context)


class SystemStateView(CommonView):
    template_name = "blindio_monitor/system_state.html"

    @method_decorator(login_required)
    def get(self, request):
        self.prepare_top_menu("blindio_monitor.system_state")
        return render(request, self.template_name, self.context)
