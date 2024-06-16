from locators.ucmo_page_locators import UcmoPageLocators
from pages.base_actions import BasePage
from utlities.singleton import ObjectManager
from utlities import setup_logging

log = setup_logging.get_logs()


class UcmSubjects(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver)
        self.context = context
        self.state_manager = ObjectManager()

    def navigate_to_subjects(self, prg):
        try:
            self.click_link_with_text(prg)
            assert self.verify_presence_of_the_element('Computer Science, MS'), 'CS not loaded properly!'
            log.info('Page Loaded Successfully')
        except Exception as e:
            log.info(f"There is some error while loading UCM Home: {e}" , exc_info=True)

    def view_course(self, text):
        try:
            self.click_button_with_text(text)
            self.switch_to_other_tab()
            assert self.verify_presence_of_the_element('Computer Science, MS'), 'CS not loaded properly!'
        except Exception as e:
            log.info(f"Error While Hitting the button {e}",exc_info=True)

    def validate_mandate_courses(self):
        try:
            assert self.verify_presence_of_the_element('Required Graduate Courses')
        except Exception as e:
            log.info(f"There are no Mandate Subjects for this Course {e}" , exc_info=True)
