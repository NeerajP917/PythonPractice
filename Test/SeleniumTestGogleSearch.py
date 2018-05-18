import unittest
from selenium import webdriver


class SearchText(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver= webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get("https://www.google.com")

    def test_SearchText(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Selenium")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__=='__main__':
    unittest.main ()