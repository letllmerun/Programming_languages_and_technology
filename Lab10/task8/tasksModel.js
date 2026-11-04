// Массив для хранения задач
const tasks = [];

// Именованный экспорт функции добавления задачи
export function addTask(title) {
    const newTask = {
        id: Date.now(),
        title: title
    };
    tasks.push(newTask);
    return tasks;
}

// Именованный экспорт функции удаления задачи
export function removeTask(id) {
    const index = tasks.findIndex(task => task.id === id);
    if (index !== -1) {
        tasks.splice(index, 1);
    }
    return tasks;
}

export function getTasks() {
    return tasks;
}