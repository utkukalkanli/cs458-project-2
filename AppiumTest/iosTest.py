import unittest
from appium import webdriver


class LocalIosTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Vaccine Survey iOS Demo'
    accessKey = "eyJhbGciOiJIUzI1NiJ9.eyJ4cC51IjoxMDk4Mzg3NywieHAucCI6MTA5ODM4NzYsInhwLm0iOjE2MTYwOTk2NDc0MTUsImV4cCI6MTkzMTQ1OTY4MCwiaXNzIjoiY29tLmV4cGVyaXRlc3QifQ.U_cs3cyUv6ESJRAHdYmYzsw5jQOrXsXxEYUseqXD2rc"
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['accessKey'] = self.accessKey
        self.dc['app'] = 'cloud:com.funksoulbrother.vaccine_survey'
        self.dc['bundleId'] = 'com.funksoulbrother.vaccine_survey'
        self.dc['platformName'] = 'ios'
        self.dc['deviceQuery'] = "@os='ios' and @category='PHONE'"
        self.driver = webdriver.Remote("https://cloud.seetest.io/wd/hub",self.dc)

    def testQuickStartIosNativeDemo(self):
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Username']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Password']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='loginButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='makePaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Phone']").send_keys('1234567')
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Name']").send_keys('Jon Snow')
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Amount']").send_keys('50')
        self.driver.find_element_by_xpath("xpath=//*[@text='countryButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Switzerland']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='sendPaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Yes']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='logoutButton']").click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()