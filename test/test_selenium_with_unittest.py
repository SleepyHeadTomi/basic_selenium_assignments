import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSelenium(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        return self.driver

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_print_main_title_text(self):
        self.driver.get("https://www.kimmoahola.net/selenium.html")
        main_title = self.driver.find_element(By.ID, "main-title")
        print(f"\nMain Title text: {main_title.text}")
        self.assertEquals(main_title.text, "Selenium Test Page")

    def test_radio_btn_blue(self):
        self.driver.get("https://www.kimmoahola.net/selenium.html")
        radio_btn = self.driver.find_element(By.XPATH, "/html/body/div[7]/label[3]/input")
        radio_btn.click()
        if radio_btn.is_selected():
            print("\nRadio Button blue selected")
            self.assertTrue(radio_btn.is_selected())

if __name__ == "__main__":
    unittest.main()