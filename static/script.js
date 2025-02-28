function uploadFile() {
    let fileInput = document.getElementById("fileInput").files[0];
    let task = document.getElementById("taskSelect").value;
    
    if (!fileInput) {
        alert("Please select a file!");
        return;
    }
    
    let formData = new FormData();
    formData.append("file", fileInput);
    formData.append("task", task);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Result: " + data.result;
    })
    .catch(error => console.error("Error:", error));
}
