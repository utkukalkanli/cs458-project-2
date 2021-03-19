# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

class VaccineAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #set up appium
        caps = {}
        caps["deviceName"] = "emulator-5554"
        caps["platformName"] = "android"
        caps["appPackage"] = "funksoulbrother.vaccine_survey"
        caps["appActivity"] = "funksoulbrother.vaccine_survey.MainActivity"
        caps["noReset"] = True
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 20)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def write_text(self, text):
        for letter in text:
            if(letter.isupper()):
                print("UPPER")
                letter = letter.lower()
                self.driver.press_keycode(60)
            cur_letter_key = ord(letter)
            if (cur_letter_key >= 97  and cur_letter_key <= 122):
                self.driver.press_keycode(cur_letter_key - 68)
            elif (cur_letter_key >= 48  and cur_letter_key <= 57):
                self.driver.press_keycode(cur_letter_key - 41)

    def check_submit_exists(self):
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(1)
        submit_btn = self.driver.find_elements_by_accessibility_id('Submit')
        self.driver.implicitly_wait(20)
        return len(submit_btn) == 1

    def test_case1(self):
        name_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")
        name_field.click()

        sleep(5)

        # Send Keys Won't Work for some reason.
        # name_field.send_keys('Ahmet')
        self.write_text('Ahmet4')

        surname_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]")
        surname_field.click()

        sleep(5)
        self.write_text("Mehmetoglu5")

        # Back
        self.driver.press_keycode(4)

        # Selecting Birth Date
        birth_date = self.driver.find_element_by_accessibility_id("Select birth date")
        birth_date.click()
        select_year_btn = self.driver.find_element_by_accessibility_id("Select year")
        select_year_btn.click()

        sleep(2)

        TouchAction(self.driver)   .long_press(x=707, y=1000)   .move_to(x=707, y=1400)   .release()   .perform()
        TouchAction(self.driver)   .long_press(x=707, y=1000)   .move_to(x=707, y=1400)   .release()   .perform()

        sleep(1)
            
        btn_1990 = self.driver.find_element_by_accessibility_id("1990")
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

    def test_case2(self):
        name_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]")
        name_field.click()

        sleep(5)

        # Send Keys Won't Work for some reason.
        # name_field.send_keys('Ahmet')
        self.write_text('Mahmux')
        # self.driver.reset()
        # Back
        self.driver.press_keycode(4)

        



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VaccineAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)