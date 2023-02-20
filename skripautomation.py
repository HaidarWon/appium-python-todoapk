from appium import webdriver
import time
from desirecaps import *

#desired_caps = {}

#desired_caps['platformName'] = 'Android'
#desired_caps['deviceName'] = 'VirtualDevice_Pixel3a_API30'
#desired_caps['appPackage'] = 'blueangels.com.todo'
#desired_caps['appActivity'] = 'blueangels.com.todo.TodoListActivity'

#driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


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
driver.find_element('id','blueangels.com.todo:id/fab').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/subject_edittext').send_keys('Night Session 2')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').click()
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/description_edittext').send_keys('Belajar Automation Aplikasi TODO android')
time.sleep(1)
driver.find_element('id','blueangels.com.todo:id/add_record').click()
time.sleep(3)

# Jika terdapat 2 list todo, dan ingin menghapus list kedua(yg terakhir), maka pakai xpath yang ini. jika ada 2 list atau lebih.. id nya tidak tersedia
# Jika yg ingin dihapus list todo yg pertama.. maka RelativeLayout[2] diganti jadi angka 1
driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.ImageView').click()
driver.find_element('id','blueangels.com.todo:id/btn_delete').click()
time.sleep(1)



#driver.find_element('id','blueangels.com.todo:id/img').click()
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/subject_edittext').click()
#driver.find_element('id','blueangels.com.todo:id/subject_edittext').clear()
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/subject_edittext').send_keys('Edit Title Success')
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/description_edittext').click()
#driver.find_element('id','blueangels.com.todo:id/description_edittext').clear()
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/description_edittext').send_keys('Edit Description Success')
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/btn_update').click()
#time.sleep(1)
#driver.find_element('id','blueangels.com.todo:id/img').click()
#driver.find_element('id','blueangels.com.todo:id/btn_delete').click()


#todo APK AUTOMATION APPIUM PYTHON by:Haidar