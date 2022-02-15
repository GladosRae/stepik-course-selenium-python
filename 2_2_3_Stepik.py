import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome('C:/drivers/chromedriver.exe')
browser.get(link)

a = int(browser.find_element(By.XPATH, "//span[@id='num1']").text)
b = int(browser.find_element(By.XPATH, "//span[@id='num2']").text)
summa = str(int(a) + int(b))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(summa)

clickSubmit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

time.sleep(4)
browser.quit()