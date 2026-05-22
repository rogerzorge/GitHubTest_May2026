"""Pytest configuration and fixtures"""

import pytest
import logging
from base_driver import BaseDriver
from config import BASE_URL

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and teardown WebDriver"""
    base_driver = BaseDriver()
    base_driver.initialize_driver()
    
    yield base_driver.driver
    
    base_driver.quit_driver()


@pytest.fixture(scope="function")
def navigate_to_base_url(driver):
    """Fixture to navigate to base URL"""
    driver.get(BASE_URL)
    logger.info(f"Navigated to {BASE_URL}")
    yield driver
