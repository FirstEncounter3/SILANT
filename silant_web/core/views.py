from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import (
    ListView,
)

from .models import (
    Machine,
    Client,
    Maintenance,
)

# Create your views here.

def unauthorized_index(request):
    if request.user.is_authenticated:
        return redirect('machine_list')
    
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        machine = Machine.objects.filter(serial_number_of_machine=serial_number).values(
                "serial_number_of_machine",
                "model_of_equipment",
                "model_of_engine",
                "serial_number_of_engine",
                "transmission_model",
                "serial_number_of_transmission",
                "drive_axle_model",
                "serial_number_of_drive_axle",
                "steering_axle_model",
                "serial_number_of_steering_axle",
            ).first()
        if machine:
            return render(request, 'index.html', {'machine': machine})
        else:
            return render(request, 'index.html', {'error_message': 'Machine not found'})
    return render(request, 'index.html')

@login_required
@permission_required('core.view_machine', raise_exception=True)
def machine_list(request):
    user_id = request.user.id
    try:
        client = Client.objects.get(user_id=user_id)
    except Client.DoesNotExist:
        return render(request, 'machine_list.html', {'error_message': 'Client not found'})

    machines = Machine.objects.filter(client=client)
    return render(request, 'machine_list.html', {'machines': machines, 'client': client})


@login_required
@permission_required('core.view_machine', raise_exception=True)
def machine_detail(request, machine_id):
    try:
        machine = Machine.objects.get(id=machine_id)
    except Machine.DoesNotExist:
        return redirect('machine_list')
    maintenances = Maintenance.objects.filter(machine_id=machine_id)
    return render(request, 'machine_detail.html', {'machine': machine, 'maintenances': maintenances})
