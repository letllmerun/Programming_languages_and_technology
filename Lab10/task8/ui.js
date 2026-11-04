// Функция отрисовки элементов списка в DOM
export function renderTaskList(container, tasks) {
    container.innerHTML = "";

    if (tasks.length === 0) {
        container.innerHTML = "<li>Список задач пуст</li>";
        return;
    }

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.style.margin = "8px 0";
        li.innerHTML = `
            <span>${task.title}</span>
            <button class="delete-btn" data-id="${task.id}" style="margin-left: 10px; color: red;">Удалить</button>
        `;
        container.appendChild(li);
    });
}