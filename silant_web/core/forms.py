from django import forms
from .models import (
    Maintenance,
    Complaint,
)


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            "maintenance_type",
            "maintenance_date",
            "operating_time",
            "work_order_number",
            "work_order_date",
            "the_organization_that_carried_out_the_maintenance",
            "machine",
            "service_company",
        ]
        widgets = {
            "maintenance_date": forms.DateInput(attrs={"type": "date"}),
            "work_order_date": forms.DateInput(attrs={"type": "date"}),
        }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            "date_of_refusal",
            "operating_time",
            "failure_node",
            "description_of_failure",
            "recovery_method",
            "parts_used",
            "recovery_date",
            "equipment_downtime",
            "machine",
            "service_company",
        ]
        widgets = {
            "date_of_refusal": forms.DateInput(attrs={"type": "date"}),
            "recovery_date": forms.DateInput(attrs={"type": "date"}),
        }
