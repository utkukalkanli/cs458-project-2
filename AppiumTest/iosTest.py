import unittest
from appium import webdriver


class LocalIosTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Vaccine Survey iOS Demo'
    accessKey = "eyJhbGciOiJIUzI1NiJ9.eyJ4cC51IjoxMDk4Mzg3NywieHAucCI6MTA5ODM4NzYsInhwLm0iOjE2MTYwOTk2NDc0MTUsImV4cCI6MTkzMTQ1OTY4MCwiaXNzIjoiY29tLmV4cGVyaXRlc3QifQ.U_cs3cyUv6ESJRAHdYmYzsw5jQOrXsXxEYUseqXD2rc"
    driver = None

    def check_submit_exists(self):
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(1)
        submit_btn = self.driver.find_elements_by_accessibility_id('Submit')
        self.driver.implicitly_wait(20)
        return len(submit_btn) == 1

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['accessKey'] = self.accessKey
        self.dc['app'] = 'cloud:com.funksoulbrother.vaccine_survey'
        self.dc['bundleId'] = 'com.funksoulbrother.vaccine_survey'
        self.dc['platformName'] = 'ios'
        self.dc['deviceQuery'] = "@os='ios' and @category='PHONE'"
        self.driver = webdriver.Remote("https://localhost:4723/wd/hub",self.dc)

    def testCase_1(self):
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Name']").send_keys('Adnan')
        self.driver.find_element_by_xpath("xpath=//*[@placeholder='Surname']").send_keys('Ziyagil')
        self.driver.press_keycode(66)

        # Selecting Birth Date
        self.driver.find_element_by_accessibility_id("Select birth date").click()
        self.driver.find_element_by_accessibility_id("Select year").click()

        TouchAction(self.driver)   .long_press(x=707, y=1000)   .move_to(x=707, y=1400)   .release()   .perform()
        TouchAction(self.driver)   .long_press(x=707, y=1000)   .move_to(x=707, y=1400)   .release()   .perform()

        btn_1990 = self.driver.find_element_by_accessibility_id("1990").click()
        btn_1990.click()
        el4 = self.driver.find_element_by_accessibility_id("Next month April 1990")
        el4.click()
        el5 = self.driver.find_element_by_accessibility_id("1, Sunday, April 1, 1990")
        el5.click()
        el6 = self.driver.find_element_by_accessibility_id("OK")
        el6.click()

        # Click City
        city_button = self.driver.find_element_by_accessibility_id("City")
        city_button.click()

        # Choose Ankara
        ankara_button = self.driver.find_element_by_accessibility_id("Ankara")
        ankara_button.click()

        # Click Gender
        gender_button = self.driver.find_element_by_accessibility_id("Gender")
        gender_button.click()

        # Choose Male
        male_button = self.driver.find_element_by_accessibility_id("Male")
        male_button.click()

        # Click Vaccince Type
        vac_type = self.driver.find_element_by_accessibility_id("Vaccine Type")
        vac_type.click()

        # Choose Type
        astra_zen = self.driver.find_element_by_accessibility_id("Oxford-Astra-Zeneca")
        astra_zen.click()

        self.assertFalse(self.check_submit_exists())

        # Choose Side Effects
        side_effects = self.driver.find_element_by_accessibility_id("Side Effects")
        side_effects.click()

        # Choose Muscle Pain
        muscle_pain = self.driver.find_element_by_accessibility_id("Muscle pain")
        muscle_pain.click()

        self.assertTrue(self.check_submit_exists())


    def testCase_2(self):


    def testCase_3(self):

    def testCase_4(self):

    def testCase_5(self):

    def tearDown(self):
        print('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()