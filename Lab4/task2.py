<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Лабораторная работа №4 — Дополнительные примеры</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Лабораторная работа №4: Валидация форм</h1>

    <!-- Переключатель вариантов -->
    <div class="level-switch">
      <button type="button" class="tab-btn active" onclick="switchLevel('employee')">Задание 10 (Средний)</button>
      <button type="button" class="tab-btn" onclick="switchLevel('event')">Задание 18 (Повышенный)</button>
    </div>

    <!-- ================= СРЕДНИЙ УРОВЕНЬ (Задание 10) ================= -->
    <section id="employee" class="level-section active">
      <h2>Анкета сотрудника</h2>
      <form id="employeeForm" novalidate>
        <div class="form-group">
          <label for="empName">ФИО *</label>
          <input type="text" id="empName" placeholder="Петров Алексей Сергеевич">
        </div>

        <div class="form-group">
          <label for="empAge">Возраст (от 18 до 70) *</label>
          <input type="number" id="empAge" placeholder="25">
        </div>

        <div class="form-group">
          <label for="empDepartment">Отдел *</label>
          <select id="empDepartment">
            <option value="">-- Выберите отдел --</option>
            <option value="IT">Отдел разработки (IT)</option>
            <option value="HR">Управление персоналом (HR)</option>
            <option value="Marketing">Маркетинг и PR</option>
            <option value="Sales">Продажи</option>
          </select>
        </div>

        <div class="form-group">
          <label>Формат работы *</label>
          <div class="radio-group">
            <label><input type="radio" name="empWorkFormat" value="офис"> Офис</label>
            <label><input type="radio" name="empWorkFormat" value="удаленка"> Удалённо</label>
            <label><input type="radio" name="empWorkFormat" value="гибрид"> Гибрид</label>
          </div>
        </div>

        <button type="submit" class="btn">Сохранить анкету</button>
        <div id="empMessage" class="message-box"></div>
      </form>
    </section>

    <!-- ================= ПОВЫШЕННЫЙ УРОВЕНЬ (Задание 18) ================= -->
    <section id="event" class="level-section">
      <h2>Бронирование мероприятия с расчётом стоимости</h2>
      <form id="eventForm" novalidate>
        <div class="form-group">
          <label for="eventUserName">ФИО *</label>
          <input type="text" id="eventUserName" placeholder="Смирнова Анна Игоревна">
        </div>

        <div class="form-group">
          <label for="eventUserEmail">E-mail *</label>
          <input type="email" id="eventUserEmail" placeholder="anna@mail.com">
        </div>

        <div class="form-group">
          <label for="eventCategory">Категория билета *</label>
          <select id="eventCategory">
            <option value="">-- Выберите категорию --</option>
            <option value="standard" data-price="1000">Стандарт (1 000 ₸)</option>
            <option value="vip" data-price="2500">VIP (2 500 ₸)</option>
            <option value="premium" data-price="5000">Премиум (5 000 ₸)</option>
          </select>
        </div>

        <div class="form-group">
          <label for="eventTicketsCount">Количество билетов (от 1 до 10) *</label>
          <input type="number" id="eventTicketsCount" value="1" min="1" max="10">
        </div>

        <div class="form-group">
          <label>Дополнительные опции:</label>
          <div class="checkbox-list">
            <label><input type="checkbox" class="event-addon" data-price="500"> Обеденный сет (+500 ₸)</label>
            <label><input type="checkbox" class="event-addon" data-price="300"> Сертификат участника (+300 ₸)</label>
            <label><input type="checkbox" class="event-addon" data-price="1000"> Парковочное место (+1 000 ₸)</label>
          </div>
        </div>

        <!-- Поле с динамическим расчётом -->
        <div class="total-price-card">
          Итоговая стоимость: <span id="totalPrice">0</span> ₸
        </div>

        <button type="submit" class="btn">Забронировать</button>
        <div id="eventMessage" class="message-box"></div>
      </form>
    </section>
  </div>

  <script src="script.js"></script>
</body>
</html>
