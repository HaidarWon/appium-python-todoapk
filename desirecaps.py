from appium import webdriver
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'VirtualDevice_Pixel3a_API30'
desired_caps['appPackage'] = 'blueangels.com.todo'
desired_caps['appActivity'] = 'blueangels.com.todo.TodoListActivity'
    
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#todo APK AUTOMATION APPIUM PYTHON by:Haidar