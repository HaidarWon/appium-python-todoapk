from appium import webdriver
import time
from desirecaps import *


driver.find_element('id','blueangels.com.todo:id/fab').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').send_keys('Today Learning-Night Session')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').send_keys('Belajar Automation Aplikasi Android TODO')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/add_record').click()
time.sleep(3)
driver.find_element('id','blueangels.com.todo:id/img').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').click()
driver.find_element('id','blueangels.com.todo:id/subject_edittext').clear()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').send_keys('Edit Title Success')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').click()
driver.find_element('id','blueangels.com.todo:id/description_edittext').clear()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').send_keys('Edit Description Success')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/btn_update').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/img').click()
driver.find_element('id','blueangels.com.todo:id/btn_delete').click()

#todo APK AUTOMATION APPIUM PYTHON by:Haidar