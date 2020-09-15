import json
import os
from typing import Any

from investing_parse import REPORT_DIR_PATH
from investing_parse.core.help_function import convert_str_to_float, \
    get_all_data_sqlite
from investing_parse.core.locators import StockLocator


class Storage:
    def __init__(self, path_db=None):
        self.db = get_all_data_sqlite(path_db) if path_db else dict()

    def create_report(self, path_report: str = None) -> None:
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
        return len(self.db)


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
            price = self.stock.find_element(*StockLocator.LAST_PRICE).text
            self.last_price = convert_str_to_float(price)
        return self.last_price
