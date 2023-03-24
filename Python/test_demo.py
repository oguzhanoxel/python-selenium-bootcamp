import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
from time import sleep


class TestDemo:

	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://www.saucedemo.com/")
		self.today = str(date.today())
		Path(self.today).mkdir(exist_ok=True)

	def teardown_method(self):
		self.driver.quit()

	def test_demo(self):
		text = "Hello"
		assert text == "Hello"

	# @pytest.mark.skip()
	@pytest.mark.parametrize(
		"username,password",
		[
			("abc", "abc"),
			("test_user", "abc"),
			("1", "1")
		])
	def test_invalid_login(self, username, password):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))

		usernameInput = self.driver.find_element(By.ID, "user-name")
		passwordInput = self.driver.find_element(By.ID, "password")
		sleep(1)

		usernameInput.send_keys(username)
		passwordInput.send_keys(password)

		loginButton = self.driver.find_element(By.ID, "login-button")
		sleep(1)
		loginButton.click()
		sleep(1)
		errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")

		self.driver.save_screenshot(f"{self.today}/test-invalid-login-{username}-{password}.png")
		assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

	def waitForElementVisible(self, locator, timeout=5):
		WebDriverWait(self.driver, timeout).until(
			expected_conditions
			.visibility_of_element_located(locator))

