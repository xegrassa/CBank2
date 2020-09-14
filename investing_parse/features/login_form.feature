Feature: Пользователь входит в систему Investing

  Background: Переход на страницу логин формы с данными по умолчанию
    Given "chrome" браузер
    And Пустые Логин и Пароль
    When Открыть страницу Investing
    Then Открылась станица ru.investing
    When Открыть логин форму
    Then Открылась логин форма

  Scenario: Пользователь оставил логин и пароль пустыми
    When Пользователь пробует войти с текущим Логин и Паролем
    Then Появилось предупреждение


  Scenario: Пользователь заполнил только логин
    Given login "user@mail.ru"
    When Пользователь пробует войти с текущим Логин и Паролем
    Then Появилось предупреждение

  Scenario: Пользователь заполнил только пароль
    Given password "iampassword"
    When Пользователь пробует войти с текущим Логин и Паролем
    Then Появилось предупреждение


  Scenario Outline: Пользователь заполнил оба поля
    Given login "<login>"
    And password "<password>"
    When Пользователь пробует войти с текущим Логин и Паролем
    Then Появилось предупреждение

    Examples: Данные логин пароль
      | login | password  |
      | user1 | password1 |
      | user2 | password2 |