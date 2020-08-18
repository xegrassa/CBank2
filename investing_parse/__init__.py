import os

BASE_DIR = os.path.join(os.getcwd(), 'investing_parse')
REPORT_DIR_PATH = os.path.join(BASE_DIR, 'report')
SCREENSHOT_DIR_PATH = os.path.join(BASE_DIR, 'screenshots')
DRIVER_DIR_PATH = os.path.join(BASE_DIR, 'browser_webdriver')

CHROMEDRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'chromedriver_linux')
GECKODRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'geckodriver_linux')

CHROME = 'chrome'
FIREFOX = 'firefox'
