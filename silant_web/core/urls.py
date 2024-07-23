from django.urls import path

from .views import (
    unauthorized_index,
    machine_list,
    machine_detail,
    complaints_list,
)

urlpatterns = [
    path('', unauthorized_index, name='welcome'),
    path('machines/', machine_list, name='machine_list'),
    path('machines/<int:machine_id>/', machine_detail, name='machine_detail'),
    path('complaints/', complaints_list, name='complaints_list'),
]