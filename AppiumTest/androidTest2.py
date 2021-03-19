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
        caps["appPackage"] = "com.example.cs453_project"
        caps["appActivity"] = "com.example.cs453_project.MainActivity"
        caps["noReset"] = True
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 20)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def check_submit_exists(self):
        # self.driver.hide_keyboard()
        self.driver.implicitly_wait(1)
        submit_btn = self.driver.find_elements_by_id("com.example.cs453_project:id/button")
        self.driver.implicitly_wait(20)
        print(len(submit_btn))
        return len(submit_btn) == 1

    def test_case1(self):

        self.assertFalse(self.check_submit_exists())

        name_field = self.driver.find_element_by_id("com.example.cs453_project:id/nameedittext")
        name_field.click()
        name_field.send_keys("Artun")

        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")
        surname_field.click()
        surname_field.send_keys("Cura")

        select_data_btn = self.driver.find_element_by_id("com.example.cs453_project:id/selectDate")
        select_data_btn.click()
        select_year_btn = self.driver.find_element_by_id("android:id/date_picker_header_year")
        select_year_btn.click()
        TouchAction(self.driver)   .press(x=542, y=704)   .move_to(x=535, y=1503)   .release()   .perform()
            
        choose_year_btn = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[2]")
        choose_year_btn.click()
        date_ok_btn = self.driver.find_element_by_id("android:id/button1")
        date_ok_btn.click()

        print("Date Selected")

        city_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnercity")
        city_dropdown.click()
        chosen_city = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]")
        chosen_city.click()

        print("Date Selected")

        gender_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnersex")
        gender_dropdown.click()
        chosen_gender = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]")
        chosen_gender.click()
        vaccine_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnervaccine")
        vaccine_dropdown.click()
        chosen_vaccine = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]")
        chosen_vaccine.click()
        effect_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnersideeffect")
        effect_dropdown.click()
        chosen_effect = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]")
        chosen_effect.click()

        self.assertTrue(self.check_submit_exists())

        name_field.clear()

        self.assertFalse(self.check_submit_exists())
  
    def test_case2(self):
        valid_names = ["Ahmet", "Hasan", "Jake"]
        invalid_names = [" ", "Mahmut3", "Can*", "Azizzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"]
        name_field = self.driver.find_element_by_id("com.example.cs453_project:id/nameedittext")
        name_field.click()
        
        for cur_name in valid_names:
            name_field.send_keys(cur_name)
            self.assertEquals(name_field.text, cur_name)
        for cur_name in invalid_names:
            name_field.send_keys(cur_name)
            self.assertNotEqual(name_field.text, cur_name)

        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")
        surname_field.click()

        for cur_name in valid_names:
            surname_field.send_keys(cur_name)
            self.assertEquals(surname_field.text, cur_name)
        for cur_name in invalid_names:
            surname_field.send_keys(cur_name)
            self.assertNotEqual(surname_field.text, cur_name)

    def test_case3(self):
        self.driver.orientation = "LANDSCAPE"
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VaccineAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)