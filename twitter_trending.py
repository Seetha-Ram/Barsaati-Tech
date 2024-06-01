import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_chrome_version():
    try:
        version = subprocess.check_output(["google-chrome", "--version"]).decode("utf-8").strip().split()[-1]
        return version
    except Exception as e:
        print(f"Error fetching Chrome version: {e}")
        return None

def run_selenium_script():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_version = get_chrome_version()
    if not chrome_version:
        return "Could not determine the Chrome version installed on the server."

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version=chrome_version).install()), options=chrome_options)

    driver.set_window_size(1024, 600)
    driver.maximize_window()

    driver.get("https://x.com/?lang=en-in&mx=2")

    time.sleep(5)

    username = '@Anonymo57498152'
    password = '@Qwer1234'

    try:
        popUp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/button'))
        )
        popUp_button.click()
    except Exception as e:
        print(f"No pop-up to close: {e}")

    try:
        signIn_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span'))
        )
        signIn_button.click()
    except Exception as e:
        driver.quit()
        return f"Error during sign-in button click: {e}"
    
    time.sleep(5)

    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        )
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)
    except Exception as e:
        driver.quit()
        return f"Error during username input: {e}"
    
    time.sleep(2)

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
    except Exception as e:
        driver.quit()
        return f"Error during password input: {e}"
    
    time.sleep(5)

    try:
        trending_topics = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/section/div/div/div/div/div/div/div/span/span'))
        )[:5]

        trends = [topic.text for topic in trending_topics]
    except Exception as e:
        driver.quit()
        return f"Error during fetching trending topics: {e}"

    driver.quit()

    return {
        "trends": trends,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
