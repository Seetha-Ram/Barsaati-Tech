from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_selenium_script():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')  # Ensure GPU is disabled
    options.add_argument('window-size=1920x1080')  # Set a large window size

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1920, 1080)  # Set window size again for safety

    # Open Twitter homepage
    driver.get("https://x.com/?lang=en-in&mx=2")

    # Wait for the page to load completely
    time.sleep(5)  # Adjust the sleep time as needed

    # Log in to Twitter (optional, but recommended to see personalized trends)
    username = '@Anonymo57498152'
    password = '@Qwer1234'

    try:
        # Close any pop-up if present
        popUp_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div[1]/div/div/div/button'))
        )
        popUp_button.click()
        print("Pop-up closed successfully.")
    except Exception as e:
        print(f"No pop-up to close: {e}")

    try:
        signIn_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span'))
        )
        signIn_button.click()
        print("Sign-in button clicked.")
    except Exception as e:
        driver.quit()
        return f"Error during sign-in button click: {e}"
    
    time.sleep(5)  # Wait for the login page to load

    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
        )
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)
        print("Username entered.")
    except Exception as e:
        driver.quit()
        return f"Error during username input: {e}"
    
    time.sleep(2)  # Wait for the next input field to appear

    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        print("Password entered.")
    except Exception as e:
        driver.quit()
        return f"Error during password input: {e}"
    
    time.sleep(5)  # Wait for the home page to load

    try:
        # Fetch the top 5 trending topics under “What’s Happening” section
        trending_topics = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@data-testid="trend"]'))
        )[:5]

        # Store the trending topics in a list
        trends = [topic.text for topic in trending_topics]
        print("Trending topics found:", trends)  # Debug print
    except Exception as e:
        driver.quit()
        return f"Error during fetching trending topics: {e}"

    # Close the WebDriver
    driver.quit()

    # Return the results
    return {
        "trends": trends,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
