from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import ElementClickInterceptedException
import time

path = "/Users/apple/Desktop/chromedriver"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=web%20developer&location=" \
      "London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# creating chrome drive to access the browser

driver = webdriver.Chrome(executable_path=path)
driver.get(URL)

# click sign in buttonn
sign_in = driver.find_elements(By.LINK_TEXT, "Sign in")
sign_in[0].click()

# Enter email
email = driver.find_elements(By.NAME, "session_key")
email[0].send_keys("congas_moloch_0q@icloud.com")

# Enter password
password = driver.find_elements(By.NAME, "session_password")
password[0].send_keys("Nohjak-vucve6-darxex")

# press enter
enter = driver.find_elements(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")
enter[0].send_keys(Keys.ENTER)


time.sleep(30)
def apply():
    # click on easy apply
    apply = driver.find_elements(By.CSS_SELECTOR, ".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button"
                                                  "--primary.ember-view")
    apply[0].send_keys(Keys.ENTER)

    # enter number
    number = driver.find_elements(By.NAME, "urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2887964106,"
                                           "42559058,phoneNumber~nationalNumber)")
    # number[0].send_keys("2348090128794")

    # click next
    next_1 = driver.find_elements(By.CSS_SELECTOR,
                                  ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    next_1[0].send_keys(Keys.ENTER)

    #  review application
    review = driver.find_elements(By.CSS_SELECTOR,
                                  ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    review[0].send_keys(Keys.ENTER)

    # submit application
    submit_application = driver.find_elements(By.CSS_SELECTOR,
                                              ".artdeco-button.artdeco-button--2.artdeco-button--primary"
                                              ".ember-view")

    submit_application[0].send_keys(Keys.ENTER)


applying = True
n = 0

while applying:
    jobs = driver.find_elements(By.CSS_SELECTOR, ".disabled.ember-view.job-card-container__link.job-card-list__title")

    save = driver.find_element(By.CSS_SELECTOR,
                               ".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button"
                               "--secondary")

    for job in jobs[n:len(jobs)]:
        n += 1
        if n % 6 == 1:

            job.click()
            time.sleep(3)
            save.send_keys(Keys.ENTER)
            time.sleep(3)
            job_scroll = driver.find_element(By.CSS_SELECTOR,
                                             ".disabled.ember-view.job-card-container__link.job-card-list__title")
            time.sleep(3)
            job.send_keys(Keys.PAGE_DOWN)
        else:
            try:
                job.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                jobs = driver.find_elements(By.CSS_SELECTOR,
                                            ".disabled.ember-view.job-card-container__link.job-card-list__title")
            # save = driver.find_element(By.CSS_SELECTOR,
            #                            ".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button"
            #                            "--secondary")
            save.send_keys(Keys.ENTER)
        if n > len(jobs):
            print("hello")


