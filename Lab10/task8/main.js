import { addTask, removeTask, getTasks } from "./tasksModel.js";
import { renderTaskList } from "./ui.js";

const taskInput = document.querySelector("#task-input");
const addBtn = document.querySelector("#add-btn");
const taskListContainer = document.querySelector("#task-list");

// 1-е событие: Добавление задачи
addBtn.addEventListener("click", () => {
    const text = taskInput.value.trim();

    if (!text) {
        alert("Введите текст задачи!");
        return;
    }

    const updatedTasks = addTask(text);
    renderTaskList(taskListContainer, updatedTasks);
    taskInput.value = "";
});

// 2-е событие: Удаление задачи (делегирование событий)
taskListContainer.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-btn")) {
        const taskId = Number(event.target.dataset.id);
        const updatedTasks = removeTask(taskId);
        renderTaskList(taskListContainer, updatedTasks);
    }
});

// Первоначальный рендер
renderTaskList(taskListContainer, getTasks());