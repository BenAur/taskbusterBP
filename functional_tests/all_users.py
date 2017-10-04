# -*- coding: utf-8 -*-
from selenium import webdriver #selenium permet de simuler un browser
import unittest

class NewVisitorTest(unittest.TestCase):
	"""docstring for NewVisitorTest"""

	#lancé au début du test
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	#lancé à la fin du test
	def tearDown(self):
		self.browser.quit()

	#test
	def test_it_worked(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
	unittest.main()
