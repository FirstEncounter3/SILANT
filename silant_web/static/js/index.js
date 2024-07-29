const complaintButton = document.getElementById('complaint-button');
const generalButton = document.getElementById('general-button');
const maintenanceButton = document.getElementById('maintenance-button');
const createMaintenanceButton = document.getElementById('create_maintenance');
const createComplaintButton = document.getElementById('create_complaint');


complaintButton.addEventListener('click', () => {
    window.location.href = '/complaints/';
});

generalButton.addEventListener('click', () => {
    window.location.href = '/machines/';
});

maintenanceButton.addEventListener('click', () => {
    window.location.href = '/maintenances/';
})

if (createMaintenanceButton) {
    createMaintenanceButton.addEventListener('click', () => {
        window.location.href = '/maintenances/create/';
    })
}

if (createComplaintButton) {
    createComplaintButton.addEventListener('click', () => {
        console.log('ping')
        window.location.href = '/complaints/create/';
    })
}
