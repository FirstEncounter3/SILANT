import django_filters

from .models import (
    Machine,
    Maintenance,
    Complaint,
)

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = Machine
        fields = [
            'model_of_equipment', 
            'model_of_engine',
            'transmission_model',
            'drive_axle_model',
            'steering_axle_model',
            'serial_number_of_machine',
        ]

class MaintenanceFilter(django_filters.FilterSet):
    class Meta:
        model = Maintenance
        fields = [
            'maintenance_type',
            'service_company',
        ]


class ComplaintFilter(django_filters.FilterSet):
    class Meta:
        model = Complaint
        fields = [
            'failure_node',
            'recovery_method',
            'service_company',
        ]