from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def create_mock_records():
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=2560x1440')
    options.add_argument("--disable-blink-features")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_argument("--headless")
    options.add_argument("--verbose")

    faker = Faker()

    browser = webdriver.Chrome(options=options)
    browser.get('http://127.0.0.1:8000/')

    timeout = 2

    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys('admin')
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys('admin')
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Login')]"))).click()
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Add Record')]"))).click()
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_first_name']"))).send_keys(faker.first_name())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_last_name']"))).send_keys(faker.last_name())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_email']"))).send_keys(faker.email())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_phone']"))).send_keys(faker.phone_number())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_address']"))).send_keys(faker.address())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_city']"))).send_keys(faker.city())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_state']"))).send_keys(faker.state_abbr())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='id_zipcode']"))).send_keys(faker.zipcode())
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add Record')]"))).click()
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logout')]"))).click()
    browser.quit()


if __name__ == '__main__':
    for i in range(10):
        create_mock_records()
print('Records added!')
