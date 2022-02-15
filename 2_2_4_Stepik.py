import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('C:/drivers/chromedriver.exe')
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

a = browser.find_element(By.XPATH, "//span[@id='input_value']")
x = a.text
y = calc(x)

resultType = browser.find_element(By.XPATH, "//input[@class='form-control']")
resultType.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button")
browser.execute_script("window.scrollBy(0, 200);")

radioButton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
radioButton.click()
checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
checkbox.click()

button.click()

time.sleep(5)
browser.quit()
