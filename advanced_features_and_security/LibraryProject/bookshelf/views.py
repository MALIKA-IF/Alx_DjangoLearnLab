from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

permission_required('app_name.can_edit', raise_exception=True)
AUTH_USER_MODEL = "relationship_app.CustomUser()"