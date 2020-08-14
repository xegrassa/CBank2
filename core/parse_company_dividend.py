from core.pages import InvestingMainPage
import threading
from queue import Queue, Empty
from core.storage import WebStorage

THREAD_COUNT = 4


class ParseDividentThread(threading.Thread):
    def __init__(self, queue, driver, storage):
        threading.Thread.__init__(self)
        self.queue = queue
        self.driver = driver
        self.storage = storage

    def run(self):
        while True:
            try:
                company_name = self.queue.get(timeout=5)
            except Empty:
                self.close()
                break
            self.parse_divident(company_name)
            self.queue.task_done()

    def parse_divident(self, company_name):
        fails = 0
        while True:
            investing_main_page = InvestingMainPage(self.driver)
            try:
                investing_main_page.go_to_main_page()
                russian_stock_page = investing_main_page.go_to_russian_stocks_page()
                company_page = russian_stock_page.go_to_company(company_name)
                divident = company_page.get_divident()
            except:
                if fails > 4:
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
    web_storage = WebStorage()
    queue = Queue()
    for company_name in companies:
        queue.put(company_name)

    for _ in range(THREAD_COUNT):
        t = ParseDividentThread(queue, browser.get_browser(), web_storage)
        t.setDaemon(True)
        t.start()
    queue.join()

    for thread in threading.enumerate():
        if thread.isDaemon():
            thread.close()
    return web_storage
