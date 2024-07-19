from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
)

from .models import (
    Machine,
)

# Create your views here.

def index(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number')
        machine = Machine.objects.filter(serial_number_of_machine=serial_number).first()
        if machine:
            return render(request, 'index.html', {'machine': machine})
        else:
            return render(request, 'index.html', {'error_message': 'Machine not found'})
    else:
        return render(request, 'index.html')