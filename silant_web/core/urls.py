from django.urls import path

from .views import (
    unauthorized_index,
    machine_list,
    machine_detail,
)

urlpatterns = [
    path('', unauthorized_index, name='welcome'),
    path('machines/', machine_list, name='machine_list'),
    path('machines/<int:machine_id>/', machine_detail, name='machine_detail'),
]