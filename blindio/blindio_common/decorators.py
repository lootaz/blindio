from django.contrib.auth.decorators import login_required

login_required = login_required(login_url="/", redirect_field_name=None)
