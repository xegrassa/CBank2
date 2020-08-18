import os

BASE_DIR = os.path.join(os.getcwd(), 'investing_parse')
REPORT_DIR_PATH = os.path.join(BASE_DIR, 'report')
SCREENSHOT_DIR_PATH = os.path.join(BASE_DIR, 'screenshots')
DRIVER_DIR_PATH = os.path.join(BASE_DIR, 'browser_webdriver')

CHROMEDRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'chromedriver.exe')
GECKODRIVER_PATH = os.path.join(DRIVER_DIR_PATH, 'geckodriver.exe')

CHROME = 'chrome'
FIREFOX = 'firefox'
