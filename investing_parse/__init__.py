import os

BASE_DIR = os.path.join(os.getcwd(), 'investing_parse')
REPORT_DIR_PATH = os.path.join(BASE_DIR, 'report')
SCREENSHOT_DIR_PATH = os.path.join(BASE_DIR, 'screenshots')

if os.name == 'nt':
    DRIVER_DIR_PATH = os.path.join(BASE_DIR, 'browser_webdriver', 'nt')
elif os.name == 'posix':
    DRIVER_DIR_PATH = os.path.join(BASE_DIR, 'browser_webdriver', 'linux')
elif os.name == 'mac':
    DRIVER_DIR_PATH = os.path.join(BASE_DIR, 'browser_webdriver', 'mac')
else:
    raise Exception('Под такую систему нет драйвера')

CHROMEDRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'chromedriver')
GECKODRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'geckodriver')

CHROME = 'chrome'
FIREFOX = 'firefox'
