Feature: Parse russian stocks on ru.investing

  Scenario: Parse russian stocks
    Given "chrome" browser
    When go to "http://ru.investing.com"
    Then opened page ru.investing
    When go to menu markets
      And go to menu stocks
      And go to menu russian
      And click
    Then opened page russian stocks
    When from stocks table, get stock whose price changed on "20" percent
      And create "report.json"
    Then "report.json" file created


  Scenario: Parse company divident
    Given "report/report.json"
    When run 4 parallel parse company dividend
    Then "dividend.json" file created