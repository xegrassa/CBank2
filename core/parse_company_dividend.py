from core.pages import InvestingMainPage
from core.locators import RussianCompanyPageLocators
from selenium import webdriver

PATH_CHROME_DRIVER = 'browser_webdrver\chromedriver.exe'


def parse_divident(company_name):
    driver = webdriver.Chrome(PATH_CHROME_DRIVER)
    app = InvestingMainPage(driver)
    try:
        app.go_to_site(app.base_url)
        app._move_on_markets()._move_on_stocks()._move_on_russian()._click()
        element_table_stocks = app.get_russian_stocks_table()
        element_company = element_table_stocks.find_element(by='xpath', value=f".//a[text() = '{company_name}']")
        element_company._click()
        element_divident = app.find_element(RussianCompanyPageLocators.LOCATOR_DIVIDENDI)
    except:
        return company_name, None
    else:
        percent_divident = element_divident.text.split()[1]
        return (company_name, percent_divident)
    finally:
        app.driver.quit()
