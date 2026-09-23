<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация студента</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h1>Регистрация студента</h1>
    <p class="subtitle">Заполните форму для регистрации</p>

    <form id="studentForm">

        <div class="form-group">
            <label for="fullName">ФИО</label>
            <input type="text" id="fullName" placeholder="Введите ФИО">
            <span class="error" id="nameError"></span>
        </div>

        <div class="form-group">
            <label for="email">E-mail</label>
            <input type="email" id="email" placeholder="example@mail.com">
            <span class="error" id="emailError"></span>
        </div>

        <div class="form-group">
            <label for="course">Курс</label>
            <select id="course">
                <option value="">Выберите курс</option>
                <option value="1">1 курс</option>
                <option value="2">2 курс</option>
                <option value="3">3 курс</option>
                <option value="4">4 курс</option>
            </select>
            <span class="error" id="courseError"></span>
        </div>

        <label class="checkbox">
            <input type="checkbox" id="agreement">
            Я согласен с правилами
        </label>
        <span class="error" id="agreementError"></span>

        <button type="submit">Зарегистрироваться</button>

    </form>

    <div id="result"></div>
</div>

<script src="script.js"></script>
</body>
</html>
