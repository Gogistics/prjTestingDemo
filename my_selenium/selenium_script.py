import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
  driver = webdriver.Chrome('/Users/alantai/Desktop/my_selenium_fabric/chromedriver')
  driver.wait = WebDriverWait(driver, 5)
  return driver
 
 
def lookup(driver, query):
  driver.get('http://www.riverbed.com/products/steelhead/index.html')
  try:
    # check title
    print driver.title

    # check cookies
    print driver.get_cookies()

    # click event
    search_btn = driver.find_element_by_xpath('//*[@id="tools"]/ul/li[3]/a')
    search_btn.click()
    time.sleep(3)

    # test responsive feature
    driver.set_window_position(0, 0)
    driver.set_window_size(1200, 400)
    time.sleep(3)

    driver.set_window_position(0, 0)
    driver.set_window_size(480, 720)
    time.sleep(3)

    # test search mechanism
    search_field = driver.find_element_by_xpath('//*[@id="query"]')
    search_field.send_keys(query)
    search_field.submit()
    time.sleep(3)

    search_result = driver.find_element_by_xpath('//*[@id="totalresults"]')
    # check detail
    print search_result.get_attribute('innerHTML')
    print search_result.text
    print search_result.tag_name
    print search_result.parent
    print search_result.location
    print search_result.size
    time.sleep(3)

    search_btn.click()
    time.sleep(3)
    driver.set_window_position(0, 0)
    driver.set_window_size(768, 1024)
    time.sleep(3)

  except TimeoutException:
    print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
  driver = init_driver()
  lookup(driver, "stealhead")
  time.sleep(5)
  driver.quit()