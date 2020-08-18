Feature: Сбор информации об акциях


#  Scenario: Парсинг цен акций на investing
    Scenario: 1
    Given "chrome" браузер
    When Открыть страницу Investing
    Then Открылась станица ru.investing
    When Переходим на страницу русских акций
    Then Открылась страница русских акций
    When Собрать информацию о российских акциях, цена которых изменилась на "24"%
    And Создать отчет "report.json"
    Then Отчет создан


#  Scenario: Парсинг дивидендов компаний
    Scenario: 2
    Given Список компаний
    And "chrome" браузер
    When Парсинг дивидендов компаний
    And Создать отчет "dividend.json"
    Then Отчет создан