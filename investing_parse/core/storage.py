import json
import os
import sqlite3
import sys
from typing import Any

from investing_parse import REPORT_DIR_PATH
from investing_parse.core.locators import StockLocator


class Storage:
    def __init__(self, path_db):
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM stock_price """)
        result = cursor.fetchall()
        self.db = dict(result)
        conn.close()

    def create_report_json(self, path_report: str = None) -> None:
        if not path_report:
            path_report = os.path.join(REPORT_DIR_PATH, 'report.json')
        report_json = json.dumps(self.db, indent=4, sort_keys=True,
                                 ensure_ascii=False)
        with open(path_report, 'w') as f:
            f.write(report_json)

    def get_data(self, key: str) -> Any:
        return self.db.get(key, None)

    def set_data(self, key: str, value: Any) -> None:
        self.db[key] = value

    def get_size(self):
        """Right now not work"""
        return sys.getsizeof(self.db)


class WebStorage(Storage):
    def __init__(self):
        self.db = {}


class Stock:
    def __init__(self, stock):
        self.stock = stock
        self.last_price = None
        self.name = None

    def get_name(self):
        """Return company name"""
        if self.name is None:
            self.name = self.stock.find_element(*StockLocator.NAME).text
        return self.name

    def get_last_price(self):
        """Return current price company"""
        if self.last_price is None:
            self.last_price = self.stock.find_element(
                *StockLocator.LAST_PRICE).text
        return self.last_price
