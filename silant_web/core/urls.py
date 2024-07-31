from django.urls import path

from .views import (
    unauthorized_index,
    machine_list,
    machine_detail,
    complaints_list,
    maintenance_list,
    MaintenanceCreateView,
    ComplaintCreateView,
    MachineCreateView,
    MachineUpdateView,
)

urlpatterns = [
    path('', unauthorized_index, name='welcome'),
    path('machines/', machine_list, name='machine_list'),
    path('machines/create/', MachineCreateView.as_view(), name='machine_create'),
    path('machines/update/<int:pk>/', MachineUpdateView.as_view(), name='machine_update'),
    path('machines/<int:machine_id>/', machine_detail, name='machine_detail'),
    path('complaints/', complaints_list, name='complaints_list'),
    path('maintenances/', maintenance_list, name='maintenance_list'),
    path('maintenances/create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('complaints/create/', ComplaintCreateView.as_view(), name='complaint_create'),
]