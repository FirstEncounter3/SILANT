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

    document.getElementsByClassName("close-button")[1].addEventListener("click", () => {
        console.log("close");
        document.getElementById("summary-modal").style.display = "none";
    });
}

document.querySelectorAll(".summary-button").forEach(button => {
    button.addEventListener("click", () => {
        const summaryUrl = `equipment_model_info/${button.dataset.equipmentId}`;
        showSummaryModal(summaryUrl);
    });
})