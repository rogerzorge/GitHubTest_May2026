# Test Automation Framework Configuration

# Browser Configuration
BROWSER = "chrome"  # Options: chrome, firefox, edge, safari
BROWSER_HEADLESS = False
BROWSER_WINDOW_SIZE = "1920,1080"

# Base URL
BASE_URL = "https://www.example.com"

# Timeouts (in seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
PAGE_LOAD_TIMEOUT = 20

# Test Data
TEST_DATA = {
    "valid_username": "testuser@example.com",
    "valid_password": "TestPassword123!",
    "invalid_username": "invalid@example.com",
    "invalid_password": "wrongpassword"
}

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/test_automation.log"

# Report Configuration
REPORT_DIR = "reports"
REPORT_SCREENSHOT_ON_FAILURE = True
