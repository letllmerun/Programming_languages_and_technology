const taskInput = document.querySelector("#taskInput");
const taskList = document.querySelector("#taskList");
const completed = document.querySelector("#completed");
const notCompleted = document.querySelector("#notCompleted");

function updateStatistics() {
    let done = 0;
    let notDone = 0;

    const tasks = taskList.querySelectorAll("li");

    tasks.forEach(task => {
        if (task.classList.contains("completed")) {
            done++;
        } else {
            notDone++;
        }
    });

    completed.textContent = done;
    notCompleted.textContent = notDone;
}

function addTask() {
    const text = taskInput.value.trim();

    if (text === "") {
        return;
    }

    const task = document.createElement("li");
    const button = document.createElement("button");

    task.textContent = text + " ";
    button.textContent = "Delete";

    task.appendChild(button);
    taskList.appendChild(task);

    task.addEventListener("click", () => {
        task.classList.toggle("completed");
        updateStatistics();
    });

    button.addEventListener("click", (event) => {
        event.stopPropagation();
        task.remove();
        updateStatistics();
    });

    taskInput.value = "";
    updateStatistics();
}

document.querySelector("#addTask").addEventListener("click", addTask);