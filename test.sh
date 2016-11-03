#!/bin/bash
# Program:
# Test Automation with Node.js modules and Selenium
# History:
# 09/21/2016
export PATH=$PATH:$(pwd)/my_drivers/
option="${1}"

case ${option} in
  nodejs)
    # testing for Node.js App
    node_modules/mocha/bin/mocha test.js
    ;;
  selenium_with_report)
    # testing with Selenium
    python ./my_selenium/selenium_script.py
    ;;
  *)
    echo "`basename ${0}`: usage: [ nodejs ] | [ selenium_with_report ]"
    ;;
esac