from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    treasure_ = browser.find_element(By.ID, 'treasure')
    treasure_get = treasure_.get_attribute('valuex')
    y = calc(int(treasure_get))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    radio_button = browser.find_element(By.ID, 'robotsRule')
    radio_button.click()

    sub_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    sub_button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()