# Packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
import time

# Config
delay = 20
login_time = 30     # Time for login (in seconds)
new_msg_time = 5    # TTime for a new message (in seconds)
send_msg_time = 10   # Time for sending a message (in seconds)
country_code = 91   # Set your country code

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = quote(file.read())

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ENTER) 
        # actions.perform()

        click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
        click_btn.click()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()