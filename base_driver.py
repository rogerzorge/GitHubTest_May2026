"""Base Driver for Selenium WebDriver initialization and management"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from config import BROWSER, BROWSER_HEADLESS, IMPLICIT_WAIT, EXPLICIT_WAIT, LOG_LEVEL

# Configure logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL))
logger = logging.getLogger(__name__)


class BaseDriver:
    """Base driver class for WebDriver initialization and common actions"""

    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        """Initialize WebDriver based on configuration"""
        try:
            if BROWSER.lower() == "chrome":
                options = webdriver.ChromeOptions()
                if BROWSER_HEADLESS:
                    options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                self.driver = webdriver.Chrome(options=options)
            
            elif BROWSER.lower() == "firefox":
                options = webdriver.FirefoxOptions()
                if BROWSER_HEADLESS:
                    options.add_argument("--headless")
                self.driver = webdriver.Firefox(options=options)
            
            else:
                logger.warning(f"Browser {BROWSER} not supported. Defaulting to Chrome.")
                self.driver = webdriver.Chrome()
            
            self.driver.implicitly_wait(IMPLICIT_WAIT)
            logger.info(f"WebDriver initialized for {BROWSER}")
            
        except Exception as e:
            logger.error(f"Error initializing WebDriver: {str(e)}")
            raise

    def quit_driver(self):
        """Quit the WebDriver"""
        if self.driver:
            self.driver.quit()
            logger.info("WebDriver closed")

    def get_url(self, url):
        """Navigate to a URL"""
        try:
            self.driver.get(url)
            logger.info(f"Navigated to {url}")
        except Exception as e:
            logger.error(f"Error navigating to {url}: {str(e)}")
            raise

    def find_element(self, locator):
        """Find element by locator tuple (By.XPATH, 'xpath_value')"""
        try:
            element = WebDriverWait(self.driver, EXPLICIT_WAIT).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element found: {locator}")
            return element
        except Exception as e:
            logger.error(f"Element not found: {locator} - {str(e)}")
            raise

    def click_element(self, locator):
        """Click on an element"""
        try:
            element = self.find_element(locator)
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except Exception as e:
            logger.error(f"Error clicking element: {str(e)}")
            raise

    def send_keys(self, locator, text):
        """Send text to an input field"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            logger.info(f"Text sent to element: {locator}")
        except Exception as e:
            logger.error(f"Error sending text: {str(e)}")
            raise

    def get_text(self, locator):
        """Get text from an element"""
        try:
            element = self.find_element(locator)
            text = element.text
            logger.info(f"Text retrieved: {text}")
            return text
        except Exception as e:
            logger.error(f"Error getting text: {str(e)}")
            raise

    def wait_for_element(self, locator, timeout=None):
        """Wait for element to be visible"""
        wait_time = timeout or EXPLICIT_WAIT
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element is visible: {locator}")
            return element
        except Exception as e:
            logger.error(f"Element did not appear within {wait_time} seconds: {str(e)}")
            raise

    def take_screenshot(self, filename):
        """Take a screenshot and save it"""
        try:
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            logger.error(f"Error taking screenshot: {str(e)}")
