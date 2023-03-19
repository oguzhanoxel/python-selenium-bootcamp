from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestSaucedemo:
	def when_username_and_password_input_empty_should_return_msg(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("")
		password.send_keys("")
		sleep(1)

		login_button.click()
		error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")

		expected_message = "Epic sadface: Username is required"
		current_message = error_message_container.text
		status = expected_message == current_message

		print("\nwhen_username_and_password_input_empty_should_return_msg")
		print(f"current_message ---> {current_message}")
		print(f"expected_message ---> {expected_message}")
		print(f"STATUS ---> {status}")

		sleep(2)

	def when_password_input_empty_should_return_msg(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("abc")
		password.send_keys("")
		sleep(1)

		login_button.click()
		error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")

		expected_message = "Epic sadface: Password is required"
		current_message = error_message_container.text
		status = expected_message == current_message

		print("\nwhen_password_input_empty_should_return_msg")
		print(f"current_message ---> {current_message}")
		print(f"expected_message ---> {expected_message}")
		print(f"STATUS ---> {status}")

		sleep(2)

	def when_locked_user_given_should_return_msg(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("locked_out_user")
		password.send_keys("secret_sauce")
		sleep(1)

		login_button.click()
		error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")

		expected_message = "Epic sadface: Sorry, this user has been locked out."
		current_message = error_message_container.text
		status = expected_message == current_message

		print("\nwhen_locked_user_given_should_return_msg")
		print(f"current_message ---> {current_message}")
		print(f"expected_message ---> {expected_message}")
		print(f"STATUS ---> {status}")

		sleep(2)

	def click_error_button(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("")
		password.send_keys("")
		sleep(1)

		login_button.click()
		error_message_container = driver.find_element(By.CLASS_NAME, "error-message-container")
		error_button = driver = driver.find_element(By.CLASS_NAME, "error-button")
		sleep(1)

		error_button.click()

		print("\nclick_error_button")

		sleep(2)

	def when_standart_user_given_should_request_url(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("standard_user")
		password.send_keys("secret_sauce")
		sleep(1)

		login_button.click()
		sleep(1)

		current_url = driver.current_url
		expected_url = "https://www.saucedemo.com/inventory.html"
		status = current_url == expected_url

		print("\nwhen_standart_user_given_should_return_msg")
		print(f"current_url ---> {current_url}")
		print(f"expected_url ---> {expected_url}")
		print(f"STATUS ---> {status}")

		sleep(2)

	def when_requested_inventory_page_should_return_products(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		username = driver.find_element(By.ID, "user-name")
		password = driver.find_element(By.ID, "password")
		login_button = driver.find_element(By.ID, "login-button")
		sleep(1)

		username.send_keys("standard_user")
		password.send_keys("secret_sauce")
		sleep(1)

		login_button.click()
		sleep(1)

		items = driver.find_elements(By.CLASS_NAME, "inventory_item")
		expected_item_count = 6
		status = len(items) == expected_item_count

		print("\nwhen_requested_inventory_page_should_return_products")
		print(f"current_count ---> {len(items)}")
		print(f"expected_item_count ---> {expected_item_count}")
		print(f"STATUS ---> {status}")

		sleep(2)

testClass = TestSaucedemo()

testClass.when_username_and_password_input_empty_should_return_msg()
testClass.when_password_input_empty_should_return_msg()
testClass.when_locked_user_given_should_return_msg()
testClass.click_error_button()
testClass.when_standart_user_given_should_request_url()
testClass.when_requested_inventory_page_should_return_products()
