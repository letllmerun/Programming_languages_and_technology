const boardData = [
    { id: 1, title: "Изучить ES-модули", status: "todo" },
    { id: 2, title: "Создать проект в VS Code", status: "done" }
];

export function getBoardData() {
    return boardData;
}

export function addNewCard(title) {
    const newCard = { id: Date.now(), title, status: "todo" };
    boardData.push(newCard);
    return boardData;
}

export function moveCardStatus(cardId) {
    const card = boardData.find(c => c.id === cardId);
    if (card) {
        // Переключаем статус между "todo" и "done"
        card.status = card.status === "todo" ? "done" : "todo";
    }
    return boardData;
}