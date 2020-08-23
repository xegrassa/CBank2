Feature: Тестовые сценарии страницы Investing


  Scenario: Парсинг цен акций на investing
    Given "chrome" браузер
    When Открыть страницу Investing
    Then Открылась станица ru.investing
    When Переходим на страницу русских акций
    Then Открылась страница русских акций
    When Собрать информацию о российских акциях, цена которых изменилась на "35"%
    And Создать отчет "report.json"
    Then Отчет создан


  Scenario: Парсинг дивидендов компаний
    Given Список компаний
    And "chrome" браузер
    When Парсинг дивидендов компаний
    And Создать отчет "dividend.json"
    Then Отчет создан


  Scenario Outline: Проверка логин формы при некоректных данных
    Given "chrome" браузер
    When Открыть страницу Investing
    Then Открылась станица ru.investing
    When Открыть логин форму
    Then Открылась логин форма
    When Проверка формы на пустые поля
    Then Появилось предупреждение
    When Проверяем форму при заполненном e-mail: "<login>"
    Then Появилось предупреждение
    When Проверяем форму при заполненном e-mail и пароле "<password>"
    Then Появилось предупреждение


    Examples: account
      | login         | password  |
      | user1@mail.ru | password1 |
      | user2@mail.ru | password2 |
      | user3         | password3 |