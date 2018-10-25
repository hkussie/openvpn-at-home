import time 
import unittest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class testBeta(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_search_indeed(self):
		driver = self.driver
		driver.get("http://127.0.0.1:8001/#/login")
		self.assertIn("OpenVPN", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("Myemail@gmail.com")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	def tearDown(self):
		time.sleep(5)
		self.driver.close()

if __name__ == "__main__":
	unittest.main()