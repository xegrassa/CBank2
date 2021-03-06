# Тестовое задание на позицию автотестировщик-WEB

### Краткое описание задания:

  > 1. Написать тестовый сценарий, который собирает информацию о российских акциях, цена которых изменилась на определенный %
  > 2. Сценарий должен запускаться в 4 экземплярах параллельно для последующего поиска дивидендной доходности компании
  > 3. Необходимо протестировать форму входа: 
  >    - Поля не заполнены
  >    - Поле email заполнено

***

### Запуск скриптов осуществляеться через скрипты run_tests и run_web_interface:
  - `run_tests` - Запускает сценарии обьявленные в "features/parse_russian_stocks.feature" после чего кладет отчет о ходе теста в "report/behave.json"
  - `run_web_interface` - Запускает веб-интерфейс в котором отображает как прошли сценарии и отчет по диведендам компании

***

### Предустановки выполняются в файле behave.ini:
 - headless= [true / false] - запуск браузера в headless режиме
 - firefox_binary_path= [C:\Program Files\Mozilla Firefox\firefox.exe] - путь до exe файла firefox в Windows. В Linux не требуется  
 - browser= [chrome / firefox] - выбор браузера

### Требования:

##### Перед запуском скриптом установить зависимости: 
```
pip install -r requirements.txt
```

##### В папке "browser_webdriver" лежат версии драйверов под Win и Linux системы
  - chromedriver 84.0.4147.30 - требует Хром 84.0.4147.125
  - geckodriver 0.27.0 - требует FireFox "79.0"
  - Python 3.8.3

Если нужного драйвера нет в папке browser_webdriver 
его можно скачать:
   - https://chromedriver.chromium.org/downloads 
   - https://github.com/mozilla/geckodriver/releases/
   
В соответствии с версией браузера и ОС. 
Назвать chromedriver, geckodriver и положить в папку нужной ОС.