from django.views import View
from tools.login_decorator import login_check


# Create your views here.
class AdvanceOrderView(View):
    @login_check
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, username):
        pass
