import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage(webdriver, app_url):
    webdriver.get(app_url)

    slideshow = (By.CSS_SELECTOR, "div#slideshow0")
    carousel = (By.CSS_SELECTOR, "div#carousel0")
    cart_button = (By.CSS_SELECTOR, "#cart button")
    search_field = (By.CSS_SELECTOR, "#search input")
    search_button = (By.CSS_SELECTOR, "#search button")

    wait = WebDriverWait(webdriver, 10)

    assert wait.until(EC.visibility_of_element_located(slideshow))
    assert wait.until(EC.visibility_of_element_located(carousel))
    assert wait.until(EC.visibility_of_element_located(cart_button))
    assert wait.until(EC.visibility_of_element_located(search_field))
    assert wait.until(EC.visibility_of_element_located(search_button))


def test_catalog_page(webdriver, app_url):
    webdriver.get(app_url)

    open_catalog_page(webdriver)

    breadcrumb_menu = (By.CSS_SELECTOR, ".breadcrumb")
    left_menu = (By.CSS_SELECTOR, ".list-group")
    sort_by_select = (By.CSS_SELECTOR, "#input-sort")
    devices_on_page_select = (By.CSS_SELECTOR, "#input-limit")
    content_area = (By.CSS_SELECTOR, "#content")

    wait = WebDriverWait(webdriver, 10)

    assert wait.until(EC.visibility_of_element_located(breadcrumb_menu))
    assert wait.until(EC.visibility_of_element_located(left_menu))
    assert wait.until(EC.visibility_of_element_located(sort_by_select))
    assert wait.until(EC.visibility_of_element_located(devices_on_page_select))
    assert wait.until(EC.visibility_of_element_located(content_area))


def test_device_page(webdriver, app_url):
    webdriver.get(app_url)

    open_catalog_page(webdriver)

    open_device_card_page(webdriver)

    device_caption = (By.XPATH, "//div[@id=\"content\"]//h1")
    rating_area = (By.CSS_SELECTOR, ".rating")
    add_to_cart_button = (By.CSS_SELECTOR, "#button-cart")
    like_button = (By.XPATH, "//div[@class=\"fb-like fb_iframe_widget\"]")
    tweet_button = (By.XPATH, "//div[@class=\"tweet_iframe_widget\"]")

    wait = WebDriverWait(webdriver, 10)

    assert wait.until(EC.visibility_of_element_located(device_caption))
    assert wait.until(EC.visibility_of_element_located(rating_area))
    assert wait.until(EC.visibility_of_element_located(add_to_cart_button))
    assert wait.until(EC.visibility_of_element_located(like_button))
    assert wait.until(EC.visibility_of_element_located(tweet_button))


def test_admin_page(webdriver, app_url):
    webdriver.get(f"{app_url}/admin/index.php")

    header_logo = (By.CSS_SELECTOR, "#header-logo")
    login_form = (By.CSS_SELECTOR, ".panel.panel-default")
    login_field = (By.XPATH, "//input[@name=\"username\"]")
    password_field = (By.XPATH, "//input[@name=\"password\"]")
    login_button = (By.XPATH, "//button[@type=\"submit\"]")

    wait = WebDriverWait(webdriver, 10)

    assert wait.until(EC.visibility_of_element_located(header_logo))
    assert wait.until(EC.visibility_of_element_located(login_form))
    assert wait.until(EC.visibility_of_element_located(login_field))
    assert wait.until(EC.visibility_of_element_located(password_field))
    assert wait.until(EC.visibility_of_element_located(login_button))


def open_catalog_page(webdriver):
    first_menu_item = (By.XPATH, "//ul[@class=\"nav navbar-nav\"]/li[1]/a")
    show_all_link = (By.CSS_SELECTOR, ".see-all")

    wait = WebDriverWait(webdriver, 10)

    wait.until(EC.element_to_be_clickable(first_menu_item)).click()
    wait.until(EC.visibility_of_element_located(show_all_link)).click()


def open_device_card_page(webdriver):
    device_caption = (By.XPATH, "//div[@id=\"content\"]/div[4]/div[1]//div[@class=\"caption\"]//a")

    WebDriverWait(webdriver, 10).until(EC.visibility_of_element_located(device_caption)).click()
