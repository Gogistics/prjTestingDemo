# -*- coding: utf-8 -*-
import time, datetime, pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
  # browser = 'Chrome'
  # driver = webdriver.Chrome('/Users/alantai/Desktop/my_selenium_fabric/chromedriver')
  browser = 'Firefox'
  driver = webdriver.Firefox('/Users/alantai/Desktop/my_selenium_fabric/') # should add geckodriver path => export PATH=$PATH:/Users/alantai/Desktop/my_selenium_fabric/
  driver.wait = WebDriverWait(driver, 5)
  return driver

def test(driver, query):
  driver.get('http://www.riverbed.com/products/steelhead/index.html')
  timestamp = str(time.time()).split('.')[0]
  test_file = open('./reports/test-report-{timestamp}.txt'.format(timestamp=timestamp), 'a')

  print '\n\n\n'
  print '<=== Start Test Automation ===>'
  print '\n'

  # write to report
  fmt = '%Y-%m-%d %H:%M:%S %Z%z'
  # current_datetime = datetime.datetime.now(tz=pytz.utc).strftime(fmt) # for UTC
  pdt = pytz.timezone('US/Pacific-New')
  current_datetime = datetime.datetime.now().replace(tzinfo=pdt).strftime(fmt) # for PDT
  test_file.write('Test Report')
  test_file.write('\n')
  test_file.write('===========')
  test_file.write('\n')
  test_file.write('Datetime ({pdt}): {current_datetime}'.format(pdt=pdt, current_datetime = current_datetime))
  test_file.write('\n')
  test_file.write('QA: {test_engineer}'.format(test_engineer='Alan Tai'))
  test_file.write('\n\n\n')

  try:
    test_file.write('Test Cases:')
    test_file.write('\n')
    # check title
    print '<--- Check Title --->'
    print driver.title
    print '\n'
    test_file.write('<--- Check Title --->')
    test_file.write('\n')
    test_file.write(u''.join(driver.title).encode('utf-8'))
    test_file.write('\n\n')

    # check cookies
    print '<--- Check Cookies --->'
    print driver.get_cookies()
    print '\n'
    test_file.write('<--- Check Cookies --->')
    test_file.write('\n')
    test_file.write(driver.get_cookies().__str__())
    test_file.write('\n\n')

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
    # search_result.value_of_css_property()
    print '<--- Check Style --->'
    print search_result.get_attribute('style')
    print '\n'
    test_file.write('<--- Check Style --->')
    test_file.write('\n')
    test_file.write(search_result.get_attribute('style').__str__())
    test_file.write('\n\n')

    # check detail
    print '<--- Check innerHTML --->'
    print search_result.get_attribute('innerHTML')
    print '\n'
    test_file.write('<--- Check innerHTML --->')
    test_file.write('\n')
    test_file.write(search_result.get_attribute('innerHTML'))
    test_file.write('\n\n')

    print '<--- Check Text of Element --->'
    print search_result.text
    print '\n'
    test_file.write('<--- Check Text of Element --->')
    test_file.write('\n')
    test_file.write(search_result.text)
    test_file.write('\n\n')

    # scroll page to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    print '<--- Check Tag Name of Element --->'
    print search_result.tag_name
    print '\n'
    test_file.write('<--- Check Tag Name of Element --->')
    test_file.write('\n')
    test_file.write(search_result.tag_name)
    test_file.write('\n\n')

    print '<--- Check Location of Element --->'
    print search_result.location
    print '\n'
    test_file.write('<--- Check Parent of Element --->')
    test_file.write('\n')
    test_file.write(str(search_result.location))
    test_file.write('\n\n')

    print '<--- Check Size of Element --->'
    print search_result.size
    print '\n'
    test_file.write('<--- Check Size of Element --->')
    test_file.write('\n')
    test_file.write(str(search_result.size))
    test_file.write('\n\n')

    time.sleep(3)

    search_btn.click()
    time.sleep(3)
    driver.set_window_position(0, 0)
    driver.set_window_size(768, 1024)
    time.sleep(3)

  except TimeoutException:
    print("Box or Button not found in riverbed.com")
  finally:
    test_file.close()
 
 
if __name__ == "__main__":
  driver = init_driver()
  test(driver, "stealhead")
  time.sleep(5)
  driver.quit()