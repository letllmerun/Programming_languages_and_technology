import { getBoardData, addNewCard, moveCardStatus } from "./columns.js";
import { renderBoard } from "./ui.js";

const cardInput = document.querySelector("#card-input");
const addCardBtn = document.querySelector("#add-card");
const boardContainer = document.querySelector("#board");

// 1-е событие: Добавление новой карточки
addCardBtn.addEventListener("click", () => {
    const title = cardInput.value.trim();
    if (!title) {
        alert("Введите название задачи!");
        return;
    }
    const updatedData = addNewCard(title);
    renderBoard(boardContainer, updatedData);
    cardInput.value = "";
});

// 2-е событие: Перемещение карточки между колонками
boardContainer.addEventListener("click", (event) => {
    if (event.target.classList.contains("move-btn")) {
        const cardId = Number(event.target.dataset.id);
        const updatedData = moveCardStatus(cardId);
        renderBoard(boardContainer, updatedData);
    }
});

// Первоначальная отрисовка
renderBoard(boardContainer, getBoardData());