import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
from time import sleep
import openpyxl
from constants import global_constants

class TestSaucedemo:
	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(global_constants.URL)
		self.today = str(date.today())
		Path(self.today).mkdir(exist_ok=True)

	def teardown_method(self):
		self.driver.quit()

	@pytest.mark.parametrize("username,password", [
		("1", "1"),
		("abc", "abc"),
		("q", "q"),
	])
	def test_when_nonexist_username_and_password_input_given_should_return_msg(self, username, password):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		password_input = self.driver.find_element(By.ID, "password")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys(username)
		password_input.send_keys(password)
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "error-message-container"))
		error_message_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")

		self.driver.save_screenshot(f"{self.today}/{self.test_when_nonexist_username_and_password_input_given_should_return_msg.__name__}-{username}-{password}.png")

		expected_message = "Epic sadface: Username and password do not match any user in this service"
		current_message = error_message_container.text

		assert expected_message == current_message

	def test_when_username_input_empty_should_return_msg(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("")
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "error-message-container"))
		error_message_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")

		self.driver.save_screenshot(f"{self.today}/{self.test_when_username_input_empty_should_return_msg.__name__}.png")

		expected_message = "Epic sadface: Username is required"
		current_message = error_message_container.text

		assert expected_message == current_message

	def test_when_password_input_empty_should_return_msg(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		password_input = self.driver.find_element(By.ID, "password")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("abc")
		password_input.send_keys("")
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "error-message-container"))
		error_message_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")

		self.driver.save_screenshot(f"{self.today}/{self.test_when_password_input_empty_should_return_msg.__name__}.png")

		expected_message = "Epic sadface: Password is required"
		current_message = error_message_container.text

		assert expected_message == current_message

	def test_when_locked_user_given_should_return_msg(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		password_input = self.driver.find_element(By.ID, "password")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("locked_out_user")
		password_input.send_keys("secret_sauce")
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "error-message-container"))
		error_message_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")

		self.driver.save_screenshot(f"{self.today}/{self.test_when_locked_user_given_should_return_msg.__name__}.png")

		expected_message = "Epic sadface: Sorry, this user has been locked out."
		current_message = error_message_container.text

		assert expected_message == current_message

	def test_close_error_message_container(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("")
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "error-message-container"))
		self.waitForElementVisible((By.CLASS_NAME, "error-button"))
		error_message_container = self.driver.find_element(By.CLASS_NAME, "error-message-container")
		error_button = driver = self.driver.find_element(By.CLASS_NAME, "error-button")

		self.driver.save_screenshot(f"{self.today}/{self.test_close_error_message_container.__name__}-visible.png")
		error_button.click()
		self.driver.save_screenshot(f"{self.today}/{self.test_close_error_message_container.__name__}-clicked.png")


	def test_when_standart_user_given_should_request_url(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		password_input = self.driver.find_element(By.ID, "password")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("standard_user")
		password_input.send_keys("secret_sauce")
		login_button.click()

		current_url = self.driver.current_url
		expected_url = f"{global_constants.URL}inventory.html"

		self.driver.save_screenshot(f"{self.today}/{self.test_when_standart_user_given_should_request_url.__name__}.png")

		assert expected_url == current_url

	def test_when_requested_inventory_page_should_return_products(self):
		self.waitForElementVisible((By.ID, "user-name"))
		self.waitForElementVisible((By.ID, "password"))
		self.waitForElementVisible((By.ID, "login-button"))

		username_input = self.driver.find_element(By.ID, "user-name")
		password_input = self.driver.find_element(By.ID, "password")
		login_button = self.driver.find_element(By.ID, "login-button")

		username_input.send_keys("standard_user")
		password_input.send_keys("secret_sauce")
		login_button.click()

		self.waitForElementVisible((By.CLASS_NAME, "inventory_item"))

		self.driver.save_screenshot(f"{self.today}/{self.test_when_requested_inventory_page_should_return_products.__name__}.png")

		items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
		expected_item_count = 6

		assert len(items) == expected_item_count
	
	def waitForElementVisible(self, locator, timeout=5):
		WebDriverWait(self.driver, timeout).until(
			expected_conditions
			.visibility_of_element_located(locator))
