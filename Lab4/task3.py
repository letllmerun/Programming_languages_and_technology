<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Лабораторная работа №4 — Задание 20 (Мини-мастер)</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Лабораторная работа №4 — Задание 20</h1>
    <h2>Мини-мастер регистрации (2 шага)</h2>

    <!-- Индикатор прогресса -->
    <div class="wizard-steps">
      <div id="step1Indicator" class="wizard-step active">1. Личные данные</div>
      <div id="step2Indicator" class="wizard-step">2. Параметры аккаунта</div>
    </div>

    <form id="wizardForm" novalidate>
      <!-- БЛОК 1: Личные данные -->
      <section id="block1" class="wizard-block active">
        <div class="form-group">
          <label for="wizName">ФИО *</label>
          <input type="text" id="wizName" placeholder="Алексеев Максим Дмитриевич">
        </div>

        <div class="form-group">
          <label for="wizEmail">E-mail *</label>
          <input type="email" id="wizEmail" placeholder="maxim@example.com">
        </div>

        <div class="form-group">
          <label for="wizCity">Город *</label>
          <select id="wizCity">
            <option value="">-- Выберите город --</option>
            <option value="Алматы">Алматы</option>
            <option value="Астана">Астана</option>
            <option value="Шымкент">Шымкент</option>
            <option value="Караганда">Караганда</option>
          </select>
        </div>

        <button type="button" class="btn" onclick="goToStep2()">Далее &rarr;</button>
      </section>

      <!-- БЛОК 2: Параметры аккаунта -->
      <section id="block2" class="wizard-block">
        <div class="form-group">
          <label for="wizRole">Роль пользователя *</label>
          <select id="wizRole">
            <option value="">-- Выберите роль --</option>
            <option value="Разработчик">Разработчик</option>
            <option value="Дизайнер">Дизайнер</option>
            <option value="Менеджер">Менеджер</option>
          </select>
        </div>

        <div class="form-group">
          <label for="wizPassword">Пароль (мин. 8 символов) *</label>
          <input type="password" id="wizPassword">
        </div>

        <div class="form-group checkbox-group">
          <label>
            <input type="checkbox" id="wizSubscribe">
            Получать новости и уведомления
          </label>
        </div>

        <div class="button-group">
          <button type="button" class="btn btn-secondary" onclick="goToStep1()">&larr; Назад</button>
          <button type="submit" class="btn">Завершить регистрацию</button>
        </div>
      </section>

      <div id="wizMessage" class="message-box"></div>
    </form>

    <!-- Итоговое резюме -->
    <div id="summaryCard" class="summary-card" style="display: none;">
      <h3>Итоговое резюме профиля</h3>
      <div id="summaryContent"></div>
      <button type="button" class="btn btn-secondary" onclick="resetWizard()" style="margin-top: 15px;">Заполнить заново</button>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>
