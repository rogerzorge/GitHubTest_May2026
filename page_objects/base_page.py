"""Base Page Object Model class"""

from selenium.webdriver.common.by import By
from base_driver import BaseDriver


class BasePage(BaseDriver):
    """Base class for all page objects"""

    def __init__(self, driver=None):
        self.driver = driver

    def verify_page_title(self, expected_title):
        """Verify page title"""
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Expected title: {expected_title}, but got: {actual_title}"
        return True

    def verify_page_url(self, expected_url):
        """Verify page URL"""
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f"Expected URL to contain: {expected_url}, but got: {actual_url}"
        return True

    def is_element_visible(self, locator, timeout=None):
        """Check if element is visible"""
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False

    def is_element_present(self, locator):
        """Check if element is present in DOM"""
        try:
            self.find_element(locator)
            return True
        except:
            return False
