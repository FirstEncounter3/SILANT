from django import forms
from .models import Maintenance

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'maintenance_type',
            'maintenance_date',
            'operating_time',
            'work_order_number',
            'work_order_date',
            'the_organization_that_carried_out_the_maintenance',
            'machine',
            'service_company',
        ]
        widgets = {
            'maintenance_date': forms.DateInput(attrs={'type': 'date'}),
            'work_order_date': forms.DateInput(attrs={'type': 'date'}),
        }