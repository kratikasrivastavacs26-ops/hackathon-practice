function addTask() {

    let task = document.getElementById("taskInput").value;
    let time = document.getElementById("timeInput").value;

    if (task === "" || time === "") {
        alert("Please enter both a task and time!");
        return;
    }

    let taskList = document.getElementById("taskList");

    taskList.innerHTML += `
        <p>☐ ${task} — ${time} minutes</p>
    `;

    document.getElementById("taskInput").value = "";
    document.getElementById("timeInput").value = "";
}