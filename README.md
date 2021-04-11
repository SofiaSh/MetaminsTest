# MetaminsTest
Реализация Django приложения “Бонусный аккаунт”
Реализовать web сервис, который хранит в БД данные о бонусных аккаунтах и
транзакциях.
Функции админ панели:
  1) Добавлять новый бонусный аккаунт:
    a) Имя
    b) Фамилия
    c) Телефон
    d) номер карты
    e) баланс в баллах
  2) Редактировать, имя, фамилию, телефон
  3) Поиск по номеру карты, фамилии, телефону
  4) Удалять бонусный аккаунт
  5) Добавить транзакции:
    a) Тип транзакции (оплата, оплата бонусами, начисление бонусов)
    b) Сумма
    c) Дата
    d) Чья транзакция
  6) Просматривать транзакции, фильтр по типу и дате

Функции REST API:
   1) Получение всех бонусных аккаунтов
   2) Получение информации о бонусном аккаунте и транзакциях по номеру карты
   3) Запрос на создание новой карты
