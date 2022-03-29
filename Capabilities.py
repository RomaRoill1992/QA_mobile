from appium import webdriver


desired_capabilities = {
    'platformName': "Android",
    'platformVersion': "11",
    'automationName': 'UiAutomator2',
    'deviceName': "Roma_Android",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true",
    "skipUnlock": "false",
    "ensureWebviewsHavePages": "true",
    "nativeWebScreenshot": "true",
    "gpsEnabled": "true",
    "language": "ukr",
    "locale": "UA",
    "app": "C:\\Users\Roman\\Documents\\MobileYakabooUIautoTest\\app_binaries\\presentation-release.apk"
}



app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)