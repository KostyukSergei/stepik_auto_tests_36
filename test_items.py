from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_basket(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "The problem is you"