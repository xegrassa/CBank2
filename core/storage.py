import sqlite3
import json
import os
import os.path
from typing import Any
import sys
from selenium.webdriver.common.by import *


PATH_SQLITE_DB = '../stocks'
NAME_REPORT_FILE = '../report/report.json'


class Storage:
    def __init__(self, path_db):
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM stock_price """)
        result = cursor.fetchall()
        self.db = dict(result)
        conn.close()

    def create_report_json(self, path_report: str = None):
        if not path_report:
            path_report = os.path.join(os.getcwd(), NAME_REPORT_FILE)
        with open(path_report, 'w') as f:
            report_json = json.dumps(self.db, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(report_json)

    def get_data(self, key: str) -> Any:
        return self.db.get(key, None)

    def set_data(self, key: str, value: Any):
        self.db[key] = value

    def get_size(self):
        return sys.getsizeof(self.db)


class WebStorage(Storage):
    def __init__(self):
        self.db = {}


class Stock:
    def __init__(self, stock):
        self.price_last = stock.find_element(By.CSS_SELECTOR, 'td[class$="-last"]').text
        self.name = stock.find_element(By.CSS_SELECTOR, '.bold.left.noWrap.elp.plusIconTd a').text

    def get_name(self):
        return self.name

    def get_last_price(self):
        return self.price_last
