export function renderBoard(container, cards) {
    const todoCards = cards.filter(c => c.status === "todo");
    const doneCards = cards.filter(c => c.status === "done");

    container.innerHTML = `
        <div style="display: flex; gap: 20px;">
            <div style="flex: 1; background: #ffebee; padding: 15px; border-radius: 8px;">
                <h3>📌 Надо сделать (${todoCards.length})</h3>
                <div class="column" data-status="todo">
                    ${todoCards.map(c => `
                        <div style="background: white; padding: 10px; margin: 8px 0; border-radius: 4px; border-left: 4px solid #f44336;">
                            <span>${c.title}</span><br>
                            <button class="move-btn" data-id="${c.id}" style="margin-top: 5px; cursor: pointer;">Переместить в Готово →</button>
                        </div>
                    `).join('')}
                </div>
            </div>

            <div style="flex: 1; background: #e8f5e9; padding: 15px; border-radius: 8px;">
                <h3>✅ Готово (${doneCards.length})</h3>
                <div class="column" data-status="done">
                    ${doneCards.map(c => `
                        <div style="background: white; padding: 10px; margin: 8px 0; border-radius: 4px; border-left: 4px solid #4caf50;">
                            <span>${c.title}</span><br>
                            <button class="move-btn" data-id="${c.id}" style="margin-top: 5px; cursor: pointer;">← Вернуть в Сделать</button>
                        </div>
                    `).join('')}
                </div>
            </div>
        </div>
    `;
}