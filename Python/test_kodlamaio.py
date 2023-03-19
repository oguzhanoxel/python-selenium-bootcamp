from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Kodlamaio:
	def test_invalid_login(self):
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get("https://www.saucedemo.com/")
		sleep(1)

		usernameInput = driver.find_element(By.ID, "user-name")
		passwordInput = driver.find_element(By.ID, "password")
		sleep(1)

		usernameInput.send_keys("1")
		passwordInput.send_keys("1")

		loginButton = driver.find_element(By.ID, "login-button")
		sleep(1)
		loginButton.click()
		sleep(1)
		errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
		textResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
		print(f"1---> {errorMessage}")
		print(f"2---> {errorMessage.text}")
		print(f"3---> {textResult}")

		sleep(2)

testClass = Test_Kodlamaio()
testClass.test_invalid_login()
