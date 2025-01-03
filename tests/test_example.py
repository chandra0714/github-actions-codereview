from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_google_search():
    # Setup WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service("/path/to/chromedriver")  # Replace with your driver path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Google
        driver.get("https://www.google.com")
        assert "Google" in driver.title

        # Perform a search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python")
        search_box.submit()

        # Verify results
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        assert len(results) > 0, "No results found"

    finally:
        driver.quit()
