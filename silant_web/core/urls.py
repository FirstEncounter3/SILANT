from django.urls import path

from .views import (
    unauthorized_index,
    machine_list,
    machine_detail,
    MachineCreateView,
    MachineUpdateView,
    machine_delete,
    maintenance_list,
    MaintenanceCreateView,
    MaintenanceUpdateView,
    maintenance_delete,
    complaints_list,
    ComplaintCreateView,
    ComplaintUpdateView,
    complaint_delete,
)

urlpatterns = [
    path('', unauthorized_index, name='welcome'),
    path('machines/', machine_list, name='machine_list'),
    path('machines/create/', MachineCreateView.as_view(), name='machine_create'),
    path('machines/update/<int:pk>/', MachineUpdateView.as_view(), name='machine_update'),
    path('machines/delete/<int:machine_id>/', machine_delete, name='machine_delete'),
    path('machines/<int:machine_id>/', machine_detail, name='machine_detail'),
    path('maintenances/', maintenance_list, name='maintenance_list'),
    path('maintenances/create/', MaintenanceCreateView.as_view(), name='maintenance_create'),
    path('maintenances/update/<int:pk>/', MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('maintenances/delete/<int:maintenance_id>/', maintenance_delete, name='maintenance_delete'),
    path('complaints/', complaints_list, name='complaints_list'),
    path('complaints/create/', ComplaintCreateView.as_view(), name='complaint_create'),
    path('complaints/update/<int:pk>/', ComplaintUpdateView.as_view(), name='complaint_update'),
    path('complaints/delete/<int:complaint_id>/', complaint_delete, name='complaint_delete'),
]