Feature: Парсинг акций страницы Investing


  Scenario: Парсинг цен акций
    Given Браузер открытый на странице Investing
    When Переходим на страницу русских акций
    Then Открылась страница русских акций
    When Собрать информацию о российских акциях, цена которых изменилась на "35"%
    And Создать отчет "report.json"
    Then Отчет создан

  Scenario: Парсинг дивидендов компаний
    Given Список компаний цена которых изменилась на определенный процент
    And Браузер
    When Парсинг дивидендов компаний в 4 потока
    And Создать отчет "dividend.json"
    Then Отчет создан

  Scenario: Фейловый сценарий
    Given Браузер открытый на странице Investing
    Then Открылась логин форма