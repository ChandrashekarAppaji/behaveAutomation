# features/environment.py
import glob
import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utlities import setup_logging
import psutil


def cleanup():
    report_path = 'reports/'
    json_files = glob.glob(os.path.join(report_path, '*.json'))
    for file in json_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error while deleting file {file}: {e}")


def before_all(context):
    # Set up ChromeDriver before any feature runs
    # chrome_driver_path = 'C:\\Users\\HP\\PycharmProjects\\behaveAutomation\\drivers\\chrome.exe'
    cleanup()
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--no-sandbox')
    # options = webdriver.ChromeOptions()
    context.driver = logging.FileHandler.selenium_driver = webdriver.Chrome(service=chrome_service,
                                                                            options=chrome_options)
    context.driver.maximize_window()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def after_all(context):
    # Quit the ChromeDriver after all features have run
    context.driver.quit()
    for process in psutil.process_iter():
        if process.name() == "chromedriver" or process.name() == "Google Chrome":
            process.kill()
    #os.system("taskkill /f /im chromedriver.exe")
