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

        self.assertFalse(self.check_submit_exists())


        city_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnercity")
        city_dropdown.click()
        chosen_city = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]")
        chosen_city.click()

        gender_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnersex")
        gender_dropdown.click()
        chosen_gender = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
        chosen_gender.click()

        self.assertFalse(self.check_submit_exists())

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
            self.assertEqual(name_field.text, cur_name)
        for cur_name in invalid_names:
            name_field.send_keys(cur_name)
            self.assertNotEqual(name_field.text, cur_name)

        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")
        surname_field.click()

        for cur_name in valid_names:
            surname_field.send_keys(cur_name)
            self.assertEqual(surname_field.text, cur_name)
        for cur_name in invalid_names:
            surname_field.send_keys(cur_name)
            self.assertNotEqual(surname_field.text, cur_name)

    def test_case3(self):
        name_field = self.driver.find_element_by_id("com.example.cs453_project:id/nameedittext")
        name_field.click()
        name_field.send_keys("Artun")
        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")
        surname_field.click()
        surname_field.send_keys("Cura")

        submit_btn = self.driver.find_element_by_id("com.example.cs453_project:id/button")
        submit_btn.click()

        submit_result = self.driver.find_element_by_id("android:id/message").text
        print(submit_result)

        result_lines = submit_result.splitlines()
        final_result_lines = []
        for cur_line in result_lines:
            final_result_lines.append(cur_line.split(":")[1][1:])

        close_msg = self.driver.find_element_by_id("android:id/button1")
        close_msg.click()

        entered_date = self.driver.find_element_by_id("com.example.cs453_project:id/dateTxt").text
        entered_city = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[1]/android.widget.TextView").text
        entered_sex = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[2]/android.widget.TextView").text
        entered_vaccine = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[3]/android.widget.TextView").text
        entered_effect = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[4]/android.widget.TextView").text

        self.assertEqual(final_result_lines[0], name_field.text)
        self.assertEqual(final_result_lines[1], surname_field.text)
        self.assertEqual(final_result_lines[2], entered_date)
        self.assertEqual(final_result_lines[3], entered_city)
        self.assertEqual(final_result_lines[4], entered_sex)
        self.assertEqual(final_result_lines[5], entered_vaccine)
        self.assertEqual(final_result_lines[6], entered_effect)

    def test_case4(self):
        name_field = self.driver.find_element_by_id("com.example.cs453_project:id/nameedittext")
        self.assertFalse(name_field.is_enabled())

        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")
        self.assertFalse(surname_field.is_enabled())

        select_data_btn = self.driver.find_element_by_id("com.example.cs453_project:id/selectDate")
        self.assertFalse(select_data_btn.is_enabled())

        city_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnercity")
        self.assertFalse(city_dropdown.is_enabled())

        gender_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnersex")
        self.assertFalse(gender_dropdown.is_enabled()) 

        vaccine_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnervaccine")
        self.assertFalse(vaccine_dropdown.is_enabled())

        effect_dropdown = self.driver.find_element_by_id("com.example.cs453_project:id/spinnersideeffect")
        self.assertFalse(effect_dropdown.is_enabled())

    def test_case5(self):
        self.driver.reset()

        name_field = self.driver.find_element_by_id("com.example.cs453_project:id/nameedittext")
        surname_field = self.driver.find_element_by_id("com.example.cs453_project:id/surnameedittext")

        try:
            self.driver.implicitly_wait(0)
            entered_date = self.driver.find_element_by_id("com.example.cs453_project:id/dateTxt").text
            self.driver.implicitly_wait(20)
            print(self.assertTrue(False))
        except:
            print("DATE NOT ENTERED")

        entered_city = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[1]/android.widget.TextView").text
        entered_sex = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[2]/android.widget.TextView").text
        entered_vaccine = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[3]/android.widget.TextView").text
        entered_effect = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Spinner[4]/android.widget.TextView").text

        self.assertEqual("Name", name_field.text)
        self.assertEqual("Surname", surname_field.text)
        self.assertEqual("City", entered_city)
        self.assertEqual("Gender", entered_sex)
        self.assertEqual("Vaccine Type", entered_vaccine)
        self.assertEqual("None", entered_effect)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(VaccineAppTests)
    unittest.TextTestRunner(verbosity=2).run(suite)