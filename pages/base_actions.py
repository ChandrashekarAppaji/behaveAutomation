# pages/base_page.py
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        self.driver.get(url)

    def wait_externally(self, locator, text):
        return self.wait.until(ec.text_to_be_present_in_element(locator, text))

    def click_button(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def click_button_with_text(self, text):
        element = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='" + text + "']")))
        element.click()

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def click_link_with_text(self, text):
        element = self.wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[contains(text(), '" + text + "')])[1]")))
        element.click()

    def switch_to_other_tab(self):
        # Get the handle of the current window (parent)
        parent_window = self.driver.current_window_handle
        time.sleep(2)
        all_windows = self.driver.window_handles

        # Switch to the new tab
        for window in all_windows:
            if window != parent_window:
                self.driver.switch_to.window(window)
                break
        print(f"Switched to window: {self.driver.current_window_handle}")

    def verify_presence_of_the_element(self, text):
        return self.wait.until(ec.presence_of_element_located((By.XPATH, "(//*[contains(text(), '" + text + "')])[1]")))
