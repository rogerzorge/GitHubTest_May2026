"""Example Page Object"""

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ExamplePage(BasePage):
    """Example page object with locators and methods"""

    # Locators
    SEARCH_INPUT = (By.ID, "search_input")
    SEARCH_BUTTON = (By.ID, "search_button")
    RESULTS_LIST = (By.CLASS_NAME, "search_results")
    FIRST_RESULT = (By.XPATH, "//div[@class='search_results']/div[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_query(self, query):
        """Enter search query in search input"""
        self.send_keys(self.SEARCH_INPUT, query)

    def click_search_button(self):
        """Click search button"""
        self.click_element(self.SEARCH_BUTTON)

    def search(self, query):
        """Perform a search"""
        self.enter_search_query(query)
        self.click_search_button()

    def get_first_result(self):
        """Get text of first search result"""
        return self.get_text(self.FIRST_RESULT)

    def is_results_displayed(self):
        """Check if search results are displayed"""
        return self.is_element_visible(self.RESULTS_LIST)
