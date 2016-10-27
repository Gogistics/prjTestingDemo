# -*- coding: utf-8 -*-
# incomplete

class TestReport(object):
  ''' Test Report for generating test reports '''
  def __init__(self, browser, timestamp):
    self.__browser = browser
    self.__timestamp = timestamp
    self.__test_report = open('./my_selenium/reports/{browser}-test-report-{timestamp}.txt'.format( browser = browser, timestamp = timestamp), 'a')

  def write_to_file_meta(self, timezone, current_datetime, test_engineer):
    self.__test_report.write('Test Report for {browser}'.format(browser = self.__browser))
    self.__test_report.write('\n')
    self.__test_report.write('==========')
    self.__test_report.write('\n')
    self.__test_report.write('Datetime (Time Zone: {timezone}): {current_datetime}'.format(timezone = timezone, current_datetime = current_datetime))
    self.__test_report.write('\n')
    self.__test_report.write('QA: {test_engineer}'.format(test_engineer = test_engineer))
    self.__test_report.write('\n\n\n')

  def write_to_file_title(self):
    self.__test_report.write('Test Cases:')
    self.__test_report.write('\n')
    self.__test_report.write('==========')
    self.__test_report.write('\n\n')

  def write_to_file(self, test_case, test_info):
    print('<--- {test_case}/{browser} --->'.format(test_case = test_case, browser = self.__browser))
    print('\n')
    print(test_info)
    print('\n')

    self.__test_report.write('<--- {test_case} --->'.format(test_case = test_case))
    self.__test_report.write('\n')
    self.__test_report.write(test_info)
    self.__test_report.write('\n\n')

  def generate_screenshot(self, timestamp, driver, mode, criteria):
    driver.get_screenshot_as_file('./my_selenium/reports/screenshots/{browser}-{mode}-{criteria}-screenshot-{timestamp}.png'.format(browser = self.__browser, mode = mode, criteria = criteria, timestamp = timestamp))

  def close_file(self):
    self.__test_report.close()
