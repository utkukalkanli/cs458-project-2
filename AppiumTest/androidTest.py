# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

caps = {}
caps["deviceName"] = "emulator-5554"
caps["platformName"] = "android"
caps["appPackage"] = "funksoulbrother.vaccine_survey"
caps["appActivity"] = "funksoulbrother.vaccine_survey.MainActivity"
caps["noReset"] = True
caps["ensureWebviewsHavePages"] = True


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(20)

def write_text(text):
    for letter in text:
        cur_letter_key = ord(letter)
        driver.press_keycode(cur_letter_key - 68)

wait = WebDriverWait(driver, 20)

name_field = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]")
name_field.click()

sleep(5)

# Send Keys Won't Work for some reason.
# name_field.send_keys('Ahmet')
write_text('ahmet')

surname_field = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[2]")
surname_field.click()

sleep(5)
write_text("mehmetoglu")

# # Selecting Birth Date
# select_birth_button = driver.find_element_by_accessibility_id("Select birth date")
# select_birth_button.click()

# select_year_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="Select year"]')))
# TouchAction().tap(select_year_button)
# print("Clicked Select Year")

# wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="2007"]')))
# TouchAction(driver)   .press(x=448, y=942)   .move_to(x=495, y=1490)   .release()   .perform()
    
# button_1990 = driver.find_element_by_accessibility_id("1990")
# TouchAction().tap(button_1990)

# el7 = driver.find_element_by_accessibility_id("Next month April 1990")
# TouchAction().tap(el7)
	
# select_year_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="1, Sunday, April 1, 1990"]')))
# TouchAction().tap(el6)

# el8 = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="OK"]')))
# TouchAction().tap(el8)

# Click City
el1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="City"]')))
# el1 = driver.find_element_by_accessibility_id("City")
el1.click()

# Choose Ankara
el2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Ankara"]')))
el2.click()

# Click Gender
el3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@content-desc="Gender"]')))
el3.click()

# Choose Male
el4 = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Male"]')))
el4.click()

# Click Vaccince Type
vac_type = driver.find_element_by_accessibility_id("Vaccine Type")
vac_type.click()

# Choose Type
astra_zen = driver.find_element_by_accessibility_id("Oxford-Astra-Zeneca")
astra_zen.click()

# Choose Side Effects
side_effects = driver.find_element_by_accessibility_id("Side Effects")
side_effects.click()

# Choose Muscle Pain
muscle_pain = driver.find_element_by_accessibility_id("Muscle pain")
muscle_pain.click()


sleep(5)

driver.quit()