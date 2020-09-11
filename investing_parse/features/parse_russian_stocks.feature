Feature: Тестовые сценарии страницы Investing


  Scenario: Парсинг цен акций
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

  Scenario: Фейловый сценарий
    Given "chrome" браузер
    When Открыть страницу Investing
    Then Открылась логин форма