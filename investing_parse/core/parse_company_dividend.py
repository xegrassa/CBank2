import os
import threading
from queue import Queue, Empty

from investing_parse import SCREENSHOT_DIR_PATH
from investing_parse.core.pages import InvestingMainPage
from investing_parse.core.storage import Storage

THREAD_COUNT = 4
MAX_FAILS = 4


class ParseDividendThread(threading.Thread):
    def __init__(self, queue, driver, storage):
        threading.Thread.__init__(self)
        self.queue = queue
        self.driver = driver
        self.storage = storage

    def run(self):
        """Run thread. Get company name and parse dividend"""
        while True:
            try:
                company_name = self.queue.get(timeout=5)
            except Empty:
                self.close()
                break
            self.get_dividend(company_name)
            self.queue.task_done()

    def get_dividend(self, company_name):
        """Parse company dividend. If fails more than 4, return  None"""
        fails = 0
        while True:
            investing_main_page = InvestingMainPage(self.driver)
            try:
                investing_main_page.go_to_main_page()
                russian_stock_page = investing_main_page.go_to_russian_stocks_page()
                company_page = russian_stock_page.go_to_company(company_name)
                dividend = company_page.get_dividend()
            except:
                if fails > MAX_FAILS:
                    self.storage.set_data(company_name, None)
                    break
                print(company_name, ' не вышло спарсить')
                fails += 1
                continue
            else:
                print(company_name, 'Done')
                screenshot_path = os.path.join(SCREENSHOT_DIR_PATH, f'{company_name}_dividend.png')
                company_page.screenshot(screenshot_path)
                self.storage.set_data(company_name, dividend)
                break

    def close(self):
        self.driver.quit()


def parse_dividends(companies, browser):
    """
    Creates 4 thread and parse company dividend.
    Every thread get company name from Queue and put result to WebStorage.
    Return class WebStorage with result parse.
    Args:
        -companies: iterator company names
        -browser: is class BrowserCreator with pre-configured options
    """
    dividend_storage = Storage()
    company_queue = Queue()
    for company_name in companies:
        company_queue.put(company_name)

    for _ in range(THREAD_COUNT):
        t = ParseDividendThread(company_queue, browser.get_browser(), dividend_storage)
        t.setDaemon(True)
        t.start()
    company_queue.join()

    for thread in threading.enumerate():
        if thread.isDaemon():
            thread.close()
    return dividend_storage
