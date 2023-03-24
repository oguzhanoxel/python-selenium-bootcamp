from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Test_Kodlamaio:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://www.saucedemo.com/")

	def test_invalid_login(self):
		WebDriverWait(self.driver, 5).until(
			expected_conditions
			.visibility_of_element_located((By.ID, "user-name")))
		WebDriverWait(self.driver, 5).until(
			expected_conditions
			.visibility_of_element_located((By.ID, "password")))

		usernameInput = self.driver.find_element(By.ID, "user-name")
		passwordInput = self.driver.find_element(By.ID, "password")
		sleep(1)

		usernameInput.send_keys("1")
		passwordInput.send_keys("1")

		loginButton = self.driver.find_element(By.ID, "login-button")
		sleep(1)
		loginButton.click()
		sleep(1)
		errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
		textResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
		print(f"1---> {errorMessage}")
		print(f"2---> {errorMessage.text}")
		print(f"3---> {textResult}")

		sleep(2)

	def test_valid_login(self):
		self.driver.get("https://www.saucedemo.com/")

		WebDriverWait(self.driver, 5).until(
			expected_conditions
			.visibility_of_element_located((By.ID, "user-name")))
		usernameInput = self.driver.find_element(By.ID, "user-name")

		WebDriverWait(self.driver, 5).until(
			expected_conditions
			.visibility_of_element_located((By.ID, "password")))
		passwordInput = self.driver.find_element(By.ID, "password")
		self.driver.execute_script("window.scrollTo(0,500)")

		# Action Chains
		actions = ActionChains(self.driver)
		actions.send_keys_to_element(usernameInput, "standard_user")
		actions.send_keys_to_element(passwordInput, "secret_sauce")
		actions.perform()

		login_btn = self.driver.find_element(By.ID, "login-button")
		login_btn.click()
		sleep(3)
		print("---")

testClass = Test_Kodlamaio()
# testClass.test_invalid_login()
testClass.test_valid_login()
