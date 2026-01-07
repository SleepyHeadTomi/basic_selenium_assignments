import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options)

    driver.get("https://www.kimmoahola.net/selenium.html")

    yield driver

    driver.quit()

def test_print_main_title_text(driver):
    main_title = driver.find_element(By.ID, "main-title")
    print(f"\nMain Title text: {main_title.text}")
    assert main_title.text == "Selenium Test Page"

def test_locate_paragraph_print_text(driver):
    text_paragraph = driver.find_element(By.CSS_SELECTOR, ".text-paragraph")
    print(f"\nParagraph text: {text_paragraph.text}")
    assert text_paragraph.text == "This paragraph has a class."

def test_input_field_enter_text(driver):
    input_field = driver.find_element(By.NAME, "username")
    input_field.send_keys("igloo")
    print(f"\nInput field value: {input_field.get_attribute('value')}")
    assert input_field.get_attribute("value") == "igloo"

def test_checkbox(driver):
    checkbox2 = driver.find_element(By.NAME, "check2")
    checkbox2.click()

    if checkbox2.is_selected():
        print("\nCheckbox checked")
        assert checkbox2.is_selected() == True
    else:
        print("\nCheckbox unchecked")
        assert not checkbox2.is_selected() == True

def test_radio_btn_blue(driver):
    radio_btn = driver.find_element(By.XPATH, "/html/body/div[7]/label[3]/input")
    radio_btn.click()
    if radio_btn.is_selected():
        print("\nRadio Button blue selected")
        assert radio_btn.is_selected() == True

def test_dropdown_option_3(driver):
    dropdown = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select.select_by_visible_text("Option 3")
    print("\nDropdown Option 3 selected, value:", dropdown.get_attribute("value"))
    assert dropdown.get_attribute("value") == "option3"

def test_click_class_btn(driver):
    class_btn = driver.find_element(By.CSS_SELECTOR, ".btn-class")
    class_btn.click()

def test_click_link_with_id(driver):
    link = driver.find_element(By.ID, "link-id")
    link.click()
    print("\nLink attribute:", link.get_attribute("href"))

def test_nested_span(driver):
    nested_span = driver.find_element(By.CSS_SELECTOR, "#nested-span")
    print(f"\nNested span text: {nested_span.text}")

def test_image_id(driver):
    image_id = driver.find_element(By.ID, "image-id")
    print(f"\nAlt attribute: {image_id.get_attribute('alt')}")