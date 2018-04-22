from appium import webdriver
from page_object.business.login_business import LoginBusiness
from utils.get_by_local import GetByLocal
from time import sleep

capabilities = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",
    "app": "/Users/lvjing/Downloads/android_app_bootstrap-debug.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)


# def login():
#     sleep(5)
#     get_by_local = GetByLocal(driver)
#     file_path = "/Users/lvjing/PycharmProjects/AppiumForPython/config/local_element.ini"
#     username = get_by_local.get_element(file_path, "login_element", "username")
#     username.send_keys('12312312')
#     password = get_by_local.get_element(file_path, "login_element", "password")
#     password.send_keys('13123')
#     login_button = get_by_local.get_element(file_path, "login_element", "login_button")
#     login_button.click()
sleep(5)
LoginBusiness(driver).login()
