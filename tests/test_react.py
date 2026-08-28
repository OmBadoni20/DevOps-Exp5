from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def test_react_app():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://localhost:3000")
        time.sleep(2)

        assert "React App" in driver.title
        assert "Learn React" in driver.page_source

    finally:
        driver.quit()