from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path

from .views import *
from apps.seguridad.views import *

app_name = 'principal'

urlpatterns = [
    path('', login_required(home), name='home'),

    #seguridad views
]
