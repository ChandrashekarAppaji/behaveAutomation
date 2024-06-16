from selenium.webdriver.common.by import By


class UcmoPageLocators(object):

    academics = (By.XPATH, "(//a[text()='Academics'])[1]")
    academic_page_header = (By.XPATH, "//h2[text()='Student-Centered Academics']")
    program_list = (By.XPATH, "//div[@id='listTwo']/child::div")
    program_page_header = (By.XPATH, "//h2[text()='UCM Academic Programs']")


