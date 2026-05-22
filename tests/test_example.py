"""Example test cases"""

import pytest
import logging
from page_objects.example_page import ExamplePage
from config import BASE_URL

logger = logging.getLogger(__name__)


class TestExamplePage:
    """Test suite for Example Page"""

    def test_page_title_verification(self, driver):
        """Test to verify page title"""
        driver.get(BASE_URL)
        page = ExamplePage(driver)
        
        # This is an example - modify according to your website
        # page.verify_page_title("Expected Title")
        assert page.driver.title, "Page title should not be empty"
        logger.info(f"Page title: {page.driver.title}")

    def test_page_url_verification(self, driver):
        """Test to verify page URL"""
        driver.get(BASE_URL)
        page = ExamplePage(driver)
        
        current_url = page.driver.current_url
        assert BASE_URL in current_url, f"URL should contain {BASE_URL}"
        logger.info(f"Current URL: {current_url}")

    def test_page_loads_successfully(self, driver):
        """Test to verify page loads successfully"""
        driver.get(BASE_URL)
        
        assert driver.title, "Page should load with a title"
        logger.info("Page loaded successfully")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
