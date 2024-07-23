const complaintButton = document.getElementById('complaint-button');
const generalButton = document.getElementById('general-button');
const maintenanceButton = document.getElementById('maintenance-button');


complaintButton.addEventListener('click', () => {
    window.location.href = '/complaints/';
});
generalButton.addEventListener('click', () => {
    window.location.href = '/machines/';
});
maintenanceButton.addEventListener('click', () => {
    window.location.href = '/machines/';
})