# -*- coding: utf-8 -*-
import time, datetime, pytz, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from multiprocessing.dummy import Pool as ThreadsPool
from test_reporter import TestReport


def init_driver_info(tag = None):
  driver_info = {}
  if tag == 'chrome':
    driver_info.update({'browser': 'Chrome'})
    driver = webdriver.Chrome('/Users/alantai/Desktop/my_selenium_fabric/chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    driver_info.update({'webdriver': driver})

  elif tag == 'firefox':
    driver_info.update({'browser': 'Firefox'})
    driver = webdriver.Firefox('/Users/alantai/Desktop/my_selenium_fabric/')
    driver.wait = WebDriverWait(driver, 5)
    driver_info.update({'webdriver': driver})

  # add shared info
  driver_info.update({'url': 'http://www.riverbed.com/products/steelhead/index.html'})
  driver_info.update({'query': 'steelfusion'})

  return driver_info

def test(info_set = None):
  driver = info_set['webdriver']
  query = info_set['query']
  browser = info_set['browser']
  url = info_set['url']
  timestamp = str(time.time()).split('.')[0]

  # init TestReport and start to generate report
  test_reporter = TestReport(browser, timestamp)

  # load web page
  driver.get(url)
  print '\n\n\n'
  print '<=== Start Test Automation for {browser} ===>'.format(browser = browser)
  print '\n'

  # write_to_file to report
  fmt = '%Y-%m-%d %H:%M:%S %Z%z'
  # current_datetime = datetime.datetime.now(tz=pytz.utc).strftime(fmt) # for UTC
  pdt = pytz.timezone('US/Pacific-New') # for PDT
  current_datetime = datetime.datetime.now().replace(tzinfo = pdt).strftime(fmt) # for PDT
  test_engineer = 'Alan Tai'

  test_reporter.write_to_file_meta(pdt, current_datetime, test_engineer)
  test_reporter.write_to_file_title()

  try:
    test_reporter.write_to_file('Check Title', u''.join(driver.title).encode('utf-8'))

    test_reporter.write_to_file('Check Cookies', str(driver.get_cookies()))

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
    # search_result.value_of_css_property() # get css property

    test_reporter.write_to_file('Check Style', str(search_result.get_attribute('style')))
    test_reporter.write_to_file('Check innerHTML', search_result.get_attribute('innerHTML'))
    test_reporter.write_to_file('Check Text of Element', search_result.text)

    # scroll page to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    test_reporter.write_to_file('Check Tag Name of Element', search_result.tag_name)
    test_reporter.write_to_file('Check Location of Element', str(search_result.location))
    test_reporter.write_to_file('Check Size of Element', str(search_result.size))

    search_btn.click()
    time.sleep(3)
    driver.set_window_position(0, 0)
    driver.set_window_size(768, 1024)
    time.sleep(3)

    # test window switching
    for handle in driver.window_handles:
      driver.switch_to_window(handle)
      time.sleep(3)

  # exception handler
  except TimeoutException:
    print("Timeout!")
  except:
    print("Unexpected error:", sys.exc_info()[0])

  # quite driver and close file
  finally:
    time.sleep(5)
    driver.quit()
    test_reporter.close_file()

def test_tasks():
  driver_tags = ['chrome', 'firefox']
  drivers = [ init_driver_info(tag) for tag in driver_tags ]

  # parallel testing on both Chrome and Firefox (you can add more browsers like Opera, IE, etc. and change the poll size)
  pool = ThreadsPool(2)
  results = pool.map(test, drivers)

if __name__ == "__main__":
  test_tasks()
