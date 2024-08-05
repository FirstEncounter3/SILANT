function showSummaryModal(summaryUrl) {
    document.getElementById("summary-modal").style.display = "block";
    fetch(summaryUrl).then(response => response.json()).then(data => {
        if (data) {
            document.getElementById("object-name").innerHTML = data.name;
            document.getElementById("object-description").innerHTML = data.description;
        } else {
            alert("Произошла ошибка при получении информации");
        }
    })

    document.getElementById("close-modal").addEventListener("click", () => {
        document.getElementById("summary-modal").style.display = "none";
    });

    document.getElementById('close-button-modal-info').addEventListener("click", () => {
        document.getElementById("summary-modal").style.display = "none";
    });
}

document.querySelectorAll(".model-of-equipment").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `machines/equipment_model_info/${button.dataset.objectId}`;
        showSummaryModal(summaryUrl);
    });
})

document.querySelectorAll(".model-of-engine").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `machines/engine_model_info/${button.dataset.objectId}`;
        showSummaryModal(summaryUrl);
    });
})

document.querySelectorAll(".model-of-transmission").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `machines/transmission_model_info/${button.dataset.objectId}`;
        showSummaryModal(summaryUrl);
    });
})

document.querySelectorAll(".model-of-drive-axle").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `machines/drive_axle_model_info/${button.dataset.objectId}`;
        showSummaryModal(summaryUrl);
    });
})

document.querySelectorAll(".model-of-steering-axle").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `machines/steering_axle_model_info/${button.dataset.objectId}`;
        showSummaryModal(summaryUrl);
    });
})