from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://example.com/login"
AGENDA_URL = "https://example.com/agenda"
USERNAME = "your_username"
PASSWORD = "your_password"
TARGET_TIME = "14:00"


def login(driver):
    driver.get(LOGIN_URL)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def book_lesson(driver, target_time):
    driver.get(AGENDA_URL)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".agenda")))
    slot = driver.find_element(By.XPATH, f"//button[contains(normalize-space(.), '{target_time}')]")
    slot.click()
    confirm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm, button.book")))
    confirm.click()


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    try:
        login(driver)
        book_lesson(driver, TARGET_TIME)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
