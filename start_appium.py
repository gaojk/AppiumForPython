from appium import webdriver

capabilities = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",
    "app": "/Users/lvjing/Downloads/android_app_bootstrap-debug.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
