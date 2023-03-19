from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")


input = driver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")
sleep(2)

button = driver.find_element(By.NAME, "btnK")
button.click()
sleep(2)

link = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
link.click()

listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Count : {len(listOfCourses)}")

sleep(10)

