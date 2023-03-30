import pytest
import openpyxl
import time
import json

from pathlib import Path
from datetime import date
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


class TestSaucedemo:
	def setup_method(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(SaucedemoConstants.URL)
		self.today = str(date.today())
		Path(self.today).mkdir(exist_ok=True)

	def teardown_method(self):
		self.driver.quit()

	# @pytest.mark.parametrize("username,password", [
	# 	("1", "1"),
	# 	("abc", "abc"),
	# 	("q", "q"),
	# ])
	# def test_when_nonexist_username_and_password_input_given_should_return_msg(self, username, password):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	password_input = self.driver.find_element(By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys(username)
	# 	password_input.send_keys(password)
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME))
	# 	error_message_container = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME)

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_nonexist_username_and_password_input_given_should_return_msg.__name__}-{username}-{password}.png")

	# 	expected_message = "Epic sadface: Username and password do not match any user in this service"
	# 	current_message = error_message_container.text

	# 	assert expected_message == current_message

	# def test_when_username_input_empty_should_return_msg(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("")
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME))
	# 	error_message_container = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME)

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_username_input_empty_should_return_msg.__name__}.png")

	# 	expected_message = "Epic sadface: Username is required"
	# 	current_message = error_message_container.text

	# 	assert expected_message == current_message

	# def test_when_password_input_empty_should_return_msg(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	password_input = self.driver.find_element(By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("abc")
	# 	password_input.send_keys("")
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME))
	# 	error_message_container = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME)

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_password_input_empty_should_return_msg.__name__}.png")

	# 	expected_message = "Epic sadface: Password is required"
	# 	current_message = error_message_container.text

	# 	assert expected_message == current_message

	# def test_when_locked_user_given_should_return_msg(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	password_input = self.driver.find_element(By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("locked_out_user")
	# 	password_input.send_keys("secret_sauce")
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME))
	# 	error_message_container = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME)

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_locked_user_given_should_return_msg.__name__}.png")

	# 	expected_message = "Epic sadface: Sorry, this user has been locked out."
	# 	current_message = error_message_container.text

	# 	assert expected_message == current_message

	# def test_close_error_message_container(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("")
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME))
	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.ERROR_BUTTON_CLASS_NAME))

	# 	error_message_container = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_MESSAGE_CONTAINER_CLASS_NAME)
	# 	error_button = driver = self.driver.find_element(By.CLASS_NAME, SaucedemoConstants.ERROR_BUTTON_CLASS_NAME)

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_close_error_message_container.__name__}-visible.png")
	# 	error_button.click()
	# 	self.driver.save_screenshot(f"{self.today}/{self.test_close_error_message_container.__name__}-clicked.png")

	# def test_when_standart_user_given_should_request_url(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	password_input = self.driver.find_element(By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("standard_user")
	# 	password_input.send_keys("secret_sauce")
	# 	login_button.click()

	# 	current_url = self.driver.current_url
	# 	expected_url = f"{SaucedemoConstants.URL}inventory.html"

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_standart_user_given_should_request_url.__name__}.png")

	# 	assert expected_url == current_url

	# def test_when_requested_inventory_page_should_return_products(self):
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID))
	# 	self.waitForElementVisible((By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID))

	# 	username_input = self.driver.find_element(By.ID, SaucedemoConstants.USERNAME_ELEMENT_ID)
	# 	password_input = self.driver.find_element(By.ID, SaucedemoConstants.PASSWORD_ELEMENT_ID)
	# 	login_button = self.driver.find_element(By.ID, SaucedemoConstants.LOGIN_BUTTON_BUTTON_ID)

	# 	username_input.send_keys("standard_user")
	# 	password_input.send_keys("secret_sauce")
	# 	login_button.click()

	# 	self.waitForElementVisible((By.CLASS_NAME, SaucedemoConstants.INVENTORY_ITEM))

	# 	self.driver.save_screenshot(f"{self.today}/{self.test_when_requested_inventory_page_should_return_products.__name__}.png")

	# 	items = self.driver.find_elements(By.CLASS_NAME, SaucedemoConstants.INVENTORY_ITEM)
	# 	expected_item_count = 6

	# 	assert len(items) == expected_item_count
	
	# def waitForElementVisible(self, locator, timeout=5):
	# 	WebDriverWait(self.driver, timeout).until(
	# 		expected_conditions
	# 		.visibility_of_element_located(locator))

class TestSaucedemoWithSeleniumIDEExport:
	def setup_method(self, method):
		self.driver = webdriver.Chrome()
		self.vars = {}
	
	def teardown_method(self, method):
		self.driver.quit()
	
	def test_whennonexistusernameandpasswordinputgivenshouldreturnmsg(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("abc")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("abc")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
		assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"
		self.driver.close()
	
	def test_whenusernameinputemptyshouldreturnmsg(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
		assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"
		self.driver.close()

	def test_whenpasswordinputemptyshouldreturnmsg(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("abc")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
		assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Password is required"
		self.driver.close()

	def test_whenlockedusergivenshouldreturnmsg(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("locked_out_user")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]")))
		assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Sorry, this user has been locked out."
		self.driver.close()

	def test_whenstandartusergivenshouldrequesturl(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
		assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
		self.driver.close()

	def test_whenrequestedinventorypageshouldreturnproducts(self):
		self.driver.get("https://www.saucedemo.com/")
		self.driver.set_window_size(1936, 1048)
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
		self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
		WebDriverWait(self.driver, 0.005).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name")))
		self.vars["current_item_count"] = len(self.driver.find_elements(By.XPATH, "//a/div"))
		assert(self.vars["current_item_count"] == 6)

class SaucedemoConstants:
	URL = "https://www.saucedemo.com/"
	USERNAME_ELEMENT_ID = "user-name"
	PASSWORD_ELEMENT_ID = "password"
	LOGIN_BUTTON_BUTTON_ID = "login-button"
	ERROR_MESSAGE_CONTAINER_CLASS_NAME = "error-message-container"
	ERROR_BUTTON_CLASS_NAME = "error-button"
	INVENTORY_ITEM = "inventory_item"
