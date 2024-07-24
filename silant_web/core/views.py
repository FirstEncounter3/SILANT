from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import (
    Machine,
    Client,
    Maintenance,
    EquipmentModel,
    EngineModel,
    TransmissionModel,
    DriveAxleModel,
    SteeringAxleModel,
    Complaint,
)

from .forms import MaintenanceForm

# Create your views here.


def unauthorized_index(request):
    if request.user.is_authenticated:
        return redirect("machine_list")

    if request.method == "POST":
        serial_number = request.POST.get("serial_number")
        machine = (
            Machine.objects.filter(serial_number_of_machine=serial_number)
            .values(
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
            )
            .first()
        )

        model_of_equipment_name = (
            EquipmentModel.objects.filter(id=machine["model_of_equipment"])
            .values("name")
            .first()
        )

        model_of_engine_name = (
            EngineModel.objects.filter(id=machine["model_of_engine"])
            .values("name")
            .first()
        )

        model_of_transmission_name = (
            TransmissionModel.objects.filter(id=machine["transmission_model"])
            .values("name")
            .first()
        )

        model_of_drive_axle_name = (
            DriveAxleModel.objects.filter(id=machine["drive_axle_model"])
            .values("name")
            .first()
        )

        model_of_steering_axle_name = (
            SteeringAxleModel.objects.filter(id=machine["steering_axle_model"])
            .values("name")
            .first()
        )

        if (
            machine
            and model_of_equipment_name
            and model_of_engine_name
            and model_of_transmission_name
            and model_of_drive_axle_name
            and model_of_steering_axle_name
        ):
            return render(
                request,
                "index.html",
                {
                    "machine": machine,
                    "model_of_equipment_name": model_of_equipment_name["name"],
                    "model_of_engine_name": model_of_engine_name["name"],
                    "model_of_transmission_name": model_of_transmission_name["name"],
                    "model_of_drive_axle_name": model_of_drive_axle_name["name"],
                    "model_of_steering_axle_name": model_of_steering_axle_name["name"],
                },
            )
        else:
            return render(request, "index.html", {"error_message": "Not found"})
    return render(request, "index.html")


@login_required
@permission_required("core.view_machine", raise_exception=True)
def machine_list(request):
    user_id = request.user.id
    try:
        client = Client.objects.get(user_id=user_id)
    except Client.DoesNotExist:
        return render(
            request, "machine_list.html", {"error_message": "Client not found"}
        )

    machines = Machine.objects.filter(client=client)
    return render(
        request, "machine_list.html", {"machines": machines, "client": client}
    )


@login_required
@permission_required("core.view_machine", raise_exception=True)
@permission_required("core.view_maintenance", raise_exception=True)
def machine_detail(request, machine_id):
    try:
        machine = Machine.objects.get(id=machine_id)
    except Machine.DoesNotExist:
        return redirect("machine_list")
    maintenances = Maintenance.objects.filter(machine_id=machine_id)
    return render(
        request,
        "machine_detail.html",
        {"machine": machine, "maintenances": maintenances},
    )


@login_required
@permission_required("core.view_maintenance", raise_exception=True)
def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    return render(request, "maintenance_list.html", {"maintenances": maintenances})


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('core.add_maintenance', raise_exception=True), name='dispatch')
class MaintenanceCreateView(CreateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = "maintenance_create.html"
    success_url = '/maintenances/'


@login_required
@permission_required("core.view_complaint", raise_exception=True)
def complaints_list(request):
    complaints = Complaint.objects.all()
    return render(request, "complaints_list.html", {"complaints": complaints})
