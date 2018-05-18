import unittest
import HTMLTestRunner
import os
import SeleniumTestGogleSearch
import SeleniumGoogleHomePage

# get the directory path to output report file
dir_path = os.getcwd()

# get all tests from SearchText and HomePageTest class
search = unittest.TestLoader().loadTestsFromTestCase(SeleniumGoogleHomePage.HomePageTest)
homepage = unittest.TestLoader().loadTestsFromTestCase(SeleniumTestGogleSearch.SearchText)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([homepage, search])

# open the report file
outfile = open(dir_path + "\Result\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Automation Test Report', description='Regression Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)