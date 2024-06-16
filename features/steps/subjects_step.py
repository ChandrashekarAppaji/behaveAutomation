from behave import *

from pages.home_page import UcmHome
from pages.subjects_page import UcmSubjects
from utlities import setup_logging
from utlities.singleton import ObjectManager

log = setup_logging.get_logs()


@given('Navigate to the "{prg}" Program and Click on "{text}"')
def impl_bk(context, prg , text ):
    context.ucmSubject = UcmSubjects(context.driver, context)
    context.ucmSubject.navigate_to_subjects(prg)
    context.ucmSubject.view_course(text)


@then('Verify if there are mandate courses in "{prg}"')
def impl_bk(context, prg):
    context.ucmSubject.validate_mandate_courses()

