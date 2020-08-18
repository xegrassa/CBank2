# CBank2

Запуск скриптов осуществляеться через скрипты run_tests и run_web_interface:
  - run_tests - Запускает сценарии обьявленные в "features/parse_russian_stocks.feature" после чего кладет отчет о ходе теста в "report/behave.json"
  - run_web_interface - Запускает веб-интерфейс в котором отображает как прошли сценарии и отчет по диведендам компании


В папке "browser_webdriver" лежат версии драйверов под Win и Linux системы. Версии драйверов:
  -ChromeDriver 84.0.4147.30 - требует Хром "Версия 84.0.4147.125 (Официальная сборка), (64 бит)"
  -geckodriver-v0.27.0 - требует FireFox "79.0"
