from behave import *

from pages.home_page import UcmHome
from utlities import setup_logging
from utlities.singleton import ObjectManager

log = setup_logging.get_logs()


@given('Launch the chrome driver and navigate to Official site of UCM')
def impl_bk(context):
    context.ucmHome = UcmHome(context.driver, context)
    context.ucmHome.navigate_to_homepage()
    log.info('UCM website loaded successfully')


@then('Look for available courses list under "{prg}" and get the list of it')
def impl_bk(context, prg):
    # context.ucmHomeCourses = UcmHome(context.driver)
    context.ucmHome.access_course_list(prg)


@Given('List of available courses in UCM')
def impl_bk(context):
    state_manager = ObjectManager()
    log.info(f'Total programs found: {len(state_manager.prg_elements)}')


@Then('Validate that "{course}" is available as part of Masters Program')
def impl_bk(context, course):
    state_manager = ObjectManager()
    programs = state_manager.prg_elements
    assert any("Computer Science" in program for program in programs), ("Computer Science is not available as part of "
                                                                        "the Masters Program")

