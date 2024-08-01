from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseNotAllowed

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

from .forms import (
    MaintenanceForm,
    ComplaintForm,
    MachineForm,
)


from .filters import (
    MachineFilter,
    MaintenanceFilter,
    ComplaintFilter,
)

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
    can_add_machine = request.user.has_perm("core.add_machine")
    can_update_machine = request.user.has_perm("core.change_machine")
    can_delete_machine = request.user.has_perm("core.delete_machine")

    try:
        client = Client.objects.get(user_id=user_id)
    except Client.DoesNotExist:
        machines = Machine.objects.all()
        machine_filter = MachineFilter(request.GET, queryset=machines)
        username = request.user.username

        return render(
            request,
            "machine_list.html",
            {
                "machines": machines,
                "filter": machine_filter,
                "can_add_machine": can_add_machine,
                "can_update_machine": can_update_machine,
                "can_delete_machine": can_delete_machine,
                "username": username,
            },
        )

    machines = Machine.objects.filter(client=client)
    machine_filter = MachineFilter(request.GET, queryset=machines)

    return render(
        request,
        "machine_list.html",
        {
            "machines": machines,
            "client": client,
            "filter": machine_filter,
            "can_add_machine": can_add_machine,
            "can_update_machine": can_update_machine,
            "can_delete_machine": can_delete_machine,
        },
    )


@login_required
@permission_required("core.delete_machine", raise_exception=True)
def machine_delete(request, machine_id):
    if request.method == "DELETE":
        try:
            machine = Machine.objects.get(id=machine_id)
            if request.user.has_perm("core.delete_machine"):
                machine.delete()
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Недостаточно прав для удаления машины.",
                    },
                    status=403,
                )
        except Machine.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Машина не найдена."}, status=404
            )
    return HttpResponseNotAllowed(["DELETE"])


@login_required
@permission_required("core.view_machine", raise_exception=True)
@permission_required("core.view_maintenance", raise_exception=True)
def machine_detail(request, machine_id):
    client = None
    try:
        machine = Machine.objects.get(id=machine_id)
    except Machine.DoesNotExist:
        return redirect("machine_list")

    try:
        client = Client.objects.get(user_id=request.user.id)
    except Client.DoesNotExist:
        client = "Гость"

    maintenances = Maintenance.objects.filter(machine_id=machine_id)

    return render(
        request,
        "machine_detail.html",
        {
            "machine": machine,
            "maintenances": maintenances,
            "username": request.user.username,
            "client": client,
        },
    )


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.add_machine", raise_exception=True), name="dispatch"
)
class MachineCreateView(CreateView):
    form_class = MachineForm
    model = Machine
    template_name = "machine_create.html"
    success_url = "/machines/"


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.change_machine", raise_exception=True), name="dispatch"
)
class MachineUpdateView(UpdateView):
    form_class = MachineForm
    model = Machine
    template_name = "machine_create.html"
    success_url = "/machines/"


@login_required
@permission_required("core.view_maintenance", raise_exception=True)
def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    maintenances_filter = MaintenanceFilter(request.GET, queryset=maintenances)
    client = None

    can_add_maintenances = request.user.has_perm("core.add_maintenance")
    can_update_maintenance = request.user.has_perm("core.change_maintenance")
    can_delete_maintenance = request.user.has_perm("core.delete_maintenance")

    try:
        client = Client.objects.get(user_id=request.user.id)
    except Client.DoesNotExist:
        client = "Гость"

    return render(
        request,
        "maintenance_list.html",
        {
            "maintenances": maintenances,
            "filter": maintenances_filter,
            "can_add_maintenance": can_add_maintenances,
            "can_update_maintenance": can_update_maintenance,
            "can_delete_maintenance": can_delete_maintenance,
            "username": request.user.username,
            "client": client,
        },
    )


@login_required
@permission_required("core.delete_maintenance", raise_exception=True)
def maintenance_delete(request, maintenance_id):
    if request.method == "DELETE":
        try:
            maintenance = Maintenance.objects.get(id=maintenance_id)
            if request.user.has_perm("core.delete_maintenance"):
                maintenance.delete()
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Не хватает прав для удаления обслуживания",
                    },
                    status=403,
                )
        except Maintenance.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Обслуживание не найдено"}, status=404
            )
    return HttpResponseNotAllowed(["DELETE"])


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.add_maintenance", raise_exception=True), name="dispatch"
)
class MaintenanceCreateView(CreateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = "maintenance_create.html"
    success_url = "/maintenances/"


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.change_maintenance", raise_exception=True),
    name="dispatch",
)
class MaintenanceUpdateView(UpdateView):
    form_class = MaintenanceForm
    model = Maintenance
    template_name = "maintenance_create.html"
    success_url = "/maintenances/"


@login_required
@permission_required("core.view_complaint", raise_exception=True)
def complaints_list(request):
    complaints = Complaint.objects.all()
    complaints_filter = ComplaintFilter(request.GET, queryset=complaints)
    can_add_complaints = request.user.has_perm("core.add_complaint")
    can_update_complaints = request.user.has_perm("core.change_complaint")
    can_delete_complaints = request.user.has_perm("core.delete_complaint")
    client = None

    try:
        client = Client.objects.get(user_id=request.user.id)
    except Client.DoesNotExist:
        client = "Гость"

    return render(
        request,
        "complaints_list.html",
        {
            "complaints": complaints,
            "filter": complaints_filter,
            "can_add_complaint": can_add_complaints,
            "can_update_complaint": can_update_complaints,
            "can_delete_complaint": can_delete_complaints,
            "username": request.user.username,
            "client": client,
        },
    )


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.add_complaint", raise_exception=True), name="dispatch"
)
class ComplaintCreateView(CreateView):
    form_class = ComplaintForm
    model = Complaint
    template_name = "complaint_create.html"
    success_url = "/complaints/"


@method_decorator(login_required, name="dispatch")
@method_decorator(
    permission_required("core.change_complaint", raise_exception=True),
    name="dispatch",
)
class ComplaintUpdateView(UpdateView):
    form_class = ComplaintForm
    model = Complaint
    template_name = "complaint_create.html"
    success_url = "/complaints/"

@login_required
@permission_required("core.delete_complaint", raise_exception=True)
def complaint_delete(request, complaint_id):
    if request.method == "DELETE":
        try:
            complaint = Complaint.objects.get(id=complaint_id)
            if request.user.has_perm("core.delete_complaint"):
                complaint.delete()
                return JsonResponse({"success": True})
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Не хватает прав для удаления рекламации",
                    },
                    status=403,
                )
        except Complaint.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Рекламация не найдена"}, status=404
            )
    return HttpResponseNotAllowed(["DELETE"])