from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_shoes(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Reebok Shoes")
        self.driver.find_element_by_name("btnK").click()

    def test_search_karan(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Karan Gajjar")
        self.driver.find_element_by_name("btnK").click()

    '''@classmethod
    def tearDownClass(cls):
        driver.close()
        driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python Projects'))'''