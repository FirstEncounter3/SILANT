from django.db import models

# Create your models here.

class BaseModel(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class EquipmentModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class EngineModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class TransmissionModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class DriveAxleModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class SteeringAxleModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Client(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class ServiceCompany(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class MaintenanceType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class FailureNode(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class RecoveryMethod(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    

class Machine(models.Model):
    serial_number_of_machine = models.CharField(max_length=255)
    model_of_equipment = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)
    model_of_engine = models.ForeignKey(EngineModel, on_delete=models.CASCADE)
    serial_number_of_engine = models.CharField(max_length=255)
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE)
    serial_number_of_transmission = models.CharField(max_length=255)
    drive_axle_model = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE)
    serial_number_of_drive_axle = models.CharField(max_length=255)
    steering_axle_model = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE)
    serial_number_of_steering_axle = models.CharField(max_length=255)
    supply_contract_number_and_date = models.CharField(max_length=255)
    date_shipped_from_factory = models.DateField(null=True)
    recipient = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255, blank=True)
    equipment = models.CharField(max_length=255, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serial_number_of_machine} | {self.model_of_equipment} | {self.client}'


class Maintenance(models.Model):
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE)
    maintenance_date = models.DateField(null=True)
    operating_time = models.IntegerField()
    work_order_number = models.CharField(max_length=255)
    work_order_date = models.DateField(null=True)
    the_organization_that_carried_out_the_maintenance = models.CharField(max_length=255)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.maintenance_type} | {self.machine} | {self.maintenance_date} | {self.machine}"


class Complaint(models.Model):
    date_of_refusal = models.DateField(null=True)
    operating_time = models.IntegerField()
    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE)
    description_of_failure = models.CharField(max_length=255)
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE)
    parts_used = models.CharField(max_length=255)
    recovery_date = models.DateField(null=True)
    equipment_downtime = models.IntegerField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.failure_node} | {self.recovery_method} | {self.machine}"