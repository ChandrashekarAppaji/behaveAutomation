# pages/another_page.py
from pages.base_actions import BasePage
from locators.ucmo_page_locators import UcmoPageLocators
import logging
from selenium.webdriver.common.by import By
from utlities.singleton import ObjectManager
from utlities import setup_logging

log = setup_logging.get_logs()


class UcmHome(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver)
        self.context = context
        self.state_manager = ObjectManager()

    def navigate_to_homepage(self):
        try:
            self.open_url("https://www.ucmo.edu/")
            assert self.wait_externally(UcmoPageLocators.academics, 'Academics'), 'Home Page not loaded properly!'
            log.info('Home page of UCM loaded successfully')
        except Exception as e:
            log.info(f"There is some error while loading UCM Home: {e}")

    def access_course_list(self, prg):
        try:
            self.click_button(UcmoPageLocators.academics)
            self.wait_externally(UcmoPageLocators.academic_page_header, 'STUDENT-CENTERED ACADEMICS')
            log.info('Clicking Academics Button')
            self.click_button_with_text(prg)
            self.wait_externally(UcmoPageLocators.program_page_header, 'UCM ACADEMIC PROGRAMS')
            prg_elements = self.find_elements(UcmoPageLocators.program_list)
            self.state_manager.prg_elements = [element.text for element in prg_elements]  # Store the text of each element
        except Exception as e:
            log.info(f"There is some error while extracting course details: {e}")
