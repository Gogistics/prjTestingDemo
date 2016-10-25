# -*- coding: utf-8 -*-
import time, datetime, pytz, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from multiprocessing.dummy import Pool as ThreadsPool

class SeleniumUnitest(unittest.TestCase):
  ''' Selenium with unittest module '''
  def test_tasks(self):
    ''' Test Tasks '''

    def init_driver(tag = None):
      driver_info = {}
      if tag == 'chrome':
        driver_info.update({'browser': 'Chrome'})
        driver_info.update({'query': 'steelfusion'})
        driver = webdriver.Chrome('/Users/alantai/Desktop/my_selenium_fabric/chromedriver')
        driver.wait = WebDriverWait(driver, 5)
        driver_info.update({'webdriver': driver})

      elif tag == 'firefox':
        driver_info.update({'browser': 'Firefox'})
        driver_info.update({'query': 'steelhead'})
        driver = webdriver.Firefox('/Users/alantai/Desktop/my_selenium_fabric/')
        driver.wait = WebDriverWait(driver, 5)
        driver_info.update({'webdriver': driver})

      driver_info.update({'url': 'http://www.riverbed.com/products/steelhead/index.html'})

      return driver_info

    def test(info_set = None):
      driver = info_set['webdriver']
      query = info_set['query']
      browser = info_set['browser']
      url = info_set['url']

      driver.get(url)
      timestamp = str(time.time()).split('.')[0]
      test_file = open('./reports/{browser}-test-report-{timestamp}.txt'.format( browser = browser, timestamp = timestamp), 'a')

      print '\n\n\n'
      print '<=== Start Test Automation for {browser} ===>'.format(browser = browser)
      print '\n'

      # write to report
      fmt = '%Y-%m-%d %H:%M:%S %Z%z'
      # current_datetime = datetime.datetime.now(tz=pytz.utc).strftime(fmt) # for UTC
      pdt = pytz.timezone('US/Pacific-New')
      current_datetime = datetime.datetime.now().replace(tzinfo=pdt).strftime(fmt) # for PDT
      test_file.write('Test Report for {browser}'.format(browser = browser))
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
        print("Errors")

      finally:
        time.sleep(5)
        driver.quit()
        test_file.close()


    # tasks
    driver_tags = ['chrome', 'firefox']
    drivers = [ init_driver(tag) for tag in driver_tags ]

    # set pool
    pool = ThreadsPool(2)
    results = pool.map(test, drivers)

if __name__ == "__main__":
  unittest.main()