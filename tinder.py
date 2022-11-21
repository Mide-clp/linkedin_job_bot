from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException
import time

path = "/Users/apple/Desktop/chromedriver"
URL = "https://tinder.com/"

drivers = webdriver.Chrome(executable_path=path)
drivers.get(URL)

# click create an account
create_account = drivers.find_element(By.XPATH, '//*[@id="t-48487324"]/div/div[1]/div/main/div[1]/div/div/div/div/div['
                                                '3]/div/div[2]/button')
time.sleep(3)
create_account.send_keys(Keys.ENTER)

# Click on facebook
time.sleep(2)
facebook = drivers.find_element(By.XPATH, '//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.send_keys(Keys.ENTER)

# selecting windows to go to
time.sleep(9)
tinder_windows = drivers.window_handles[0]
facebook_windows = drivers.window_handles[1]

drivers.switch_to.window(facebook_windows)

# Enter email
facebook_email = drivers.find_element(By.NAME, "email")
facebook_email.send_keys("pad_antigen0c@icloud.com")

# enter password
facebook_password = drivers.find_element(By.NAME, "pass")
facebook_password.send_keys("nisdit-seqre8-nogKut")

# confirm
press_enter = drivers.find_element(By.CSS_SELECTOR, "#loginbutton")
press_enter.send_keys(Keys.ENTER)

# click continue to enter
time.sleep(10)
screen_numbers = drivers.window_handles
print(screen_numbers)


try:
    click_continue = drivers.find_element(By.CSS_SELECTOR, ".pq6dq46d.cbu4d94t.taijpn5t.l9j0dhe7.k4urcfbm")
    click_continue.send_keys(Keys.ENTER)
    print(click_continue)
except NoSuchElementException:
    click_continue = drivers.find_element(By.CSS_SELECTOR, ".a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5")
    print(click_continue)



# drivers.quit()
