from core.pages import SearchHelper
from core.locators import Russian_Company_Page_Locators
from selenium import webdriver

PATH_CHROME_DRIVER = 'browser_webdrver\chromedriver.exe'


def parse_divident(company_name):
    driver = webdriver.Chrome(PATH_CHROME_DRIVER)
    app = SearchHelper(driver)
    try:
        app.go_to_site()
        app.move_on_page_russian_stocks()
        element_table_stocks = app.get_russian_stocks_table()
        element_company = element_table_stocks.find_element(by='xpath', value=f".//a[text() = '{company_name}']")
        element_company.click()
        element_divident = app.find_element(Russian_Company_Page_Locators.LOCATOR_DIVIDENDI)
    except:
        return company_name, None
    else:
        percent_divident = element_divident.text.split()[1]
        return (company_name, percent_divident)
    finally:
        app.driver.quit()
