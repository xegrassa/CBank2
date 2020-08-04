Feature: Parse russian stocks on ru.investing


  Scenario: Parse russian stocks
    Given "chrome" browser
    When Открыть страницу Investing
    Then Открылась станица ru.investing
    When Переходим на страницу русских акций
    Then Открылась страница русских акций
    When Собрать информацию о российских акциях, цена которых изменилась на "24"%
    And Создать отчет "report.json"
    Then Отчет создан

#
#  Scenario: Parse company divident
#    Given "report/report.json"
#    When run 4 parallel parse company dividend
#    Then "dividend.json" file created