export function createTaskObject(title) {
    return {
        id: Date.now(),
        title: title,
        status: "todo" // Начальный статус: "Сделать"
    };
}