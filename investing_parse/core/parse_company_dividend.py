import threading
from queue import Queue, Empty

from investing_parse.core.pages import InvestingMainPage
from investing_parse.core.storage import WebStorage

THREAD_COUNT = 4
MAX_FAILS = 4


class ParseDividentThread(threading.Thread):
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
            self.parse_divident(company_name)
            self.queue.task_done()

    def parse_divident(self, company_name):
        """Parse company dividend. If fails more than 4, return  None"""
        fails = 0
        while True:
            investing_main_page = InvestingMainPage(self.driver)
            try:
                investing_main_page.go_to_main_page()
                russian_stock_page = investing_main_page.go_to_russian_stocks_page()
                company_page = russian_stock_page.go_to_company(company_name)
                divident = company_page.get_divident()
            except:
                if fails > MAX_FAILS:
                    self.storage.set_data(company_name, None)
                    break
                print(company_name, ' не вышло спарсить')
                fails += 1
                continue
            else:
                print(company_name, 'Done')
                self.storage.set_data(company_name, divident)
                break

    def close(self):
        self.driver.quit()


def parse_divident(companies, browser):
    """
    Creates 4 thread and parse company dividend.
    Every thread get company name from Queue and put result to WebStorage.
    Return class WebStorage with result parse.
    Args:
        -companies: iterator company names
        -browser: is class BrowserCreator with pre-configured options
    """
    web_storage = WebStorage()
    company_queue = Queue()
    for company_name in companies:
        company_queue.put(company_name)

    for _ in range(THREAD_COUNT):
        t = ParseDividentThread(company_queue, browser.get_browser(), web_storage)
        t.setDaemon(True)
        t.start()
    company_queue.join()

    for thread in threading.enumerate():
        if thread.isDaemon():
            thread.close()
    return web_storage
