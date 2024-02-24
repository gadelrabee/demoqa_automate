import re
import time
from selenium import webdriver
#driver = webdriver.Chrome(executable_path='path/to/chromedriver')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def is_valid_email(email):
    try:
        email_pattern =  "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

        if re.search(email_pattern,email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False



def is_valid_mobile(mobile):
    return bool(re.match(r'^\d{10}$', mobile))
driver.get("https://demoqa.com")
driver.maximize_window()
time.sleep(0)

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(0.5)

page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 200
scroll_iterations = int(page_height/scroll_speed)
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
    time.sleep(0.1)

first_name_field = driver.find_element(*(By.XPATH,"//input[@id='firstName']"))
last_name_field = driver.find_element(*(By.XPATH,"//input[@id='lastName']"))
email_field = driver.find_element(*(By.XPATH,"//input[@id='userEmail']"))
gender = driver.find_element(By.CLASS_NAME, "custom-control-label")
mobile_field = driver.find_element(*(By.XPATH,"//input[@id='userNumber']"))
date_of_birth_field = driver.find_element(*(By.XPATH,"//input[@id='dateOfBirthInput']"))
subject_field = driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
#import pdb; pdb.set_trace()

#hobbies
hobby_sports_checkbox = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']"))
)
hobby_music_checkbox = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Music']"))
)
#current address
current_address_field = driver.find_element(*(By.XPATH,"//textarea[@id='currentAddress']"))

#state_and_city
#state_element = driver.find_element(By.ID, "react-select-3-input")

first_name = "Roshan"
last_name = "Koirala"
email = "koiralarodhan@..gmail.com"
mobile = "9804243569"
date_of_birth = "23-01-1995"
#subject = "Quality Assurance"
current_address = "Patan"

if not first_name:
    print("first name cannot be empty")
first_name_field.clear()
first_name_field.send_keys(first_name)
time.sleep(0.5)

if not last_name:
    print("last name cannot be empty")
last_name_field.clear()
last_name_field.send_keys(last_name)
time.sleep(0.5)

if is_valid_email(email):
    print("valid email")
else:
    print("invalid email")
email_field.clear()
email_field.send_keys(email)
time.sleep(0.5)
if gender.is_selected():
    pass
else:
    gender.click()
time.sleep(0.5)

if not mobile:
    print("mobile number cannot be empty")
mobile_field.clear()
mobile_field.send_keys(mobile)
time.sleep(0.5)

if not date_of_birth:
    print("date of birth cannot be empty")
date_of_birth_field.clear()
date_of_birth_field.send_keys(date_of_birth)
time.sleep(0.5)

# if not subject:
#     print("subject cannot be empty")
#import pdb; pdb.set_trace()
subject_field.clear()
subject_field.send_keys("s")
time.sleep(0.5)
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
time.sleep(0.5)

driver.execute_script("arguments[0].click();", hobby_sports_checkbox)
driver.execute_script("arguments[0].click();", hobby_music_checkbox)


if not current_address:
    print("required field")
current_address_field.clear()
current_address_field.send_keys(current_address)
time.sleep(0.5)

# dropdown = Select(state_element)
# dropdown.select_by_visible_text("Uttar Pradesh")


driver.quit()
print("your code has run successfully")






