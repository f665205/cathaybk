import time
import os
import sys
from glob import glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

os.chdir(os.path.dirname(sys.argv[0]))

path = 'result.txt'
f = open(path, 'w+')

mobile_emulation={"deviceName": "iPhone SE"}
options = Options()
options.add_experimental_option("mobileEmulation",mobile_emulation)
driver = webdriver.Chrome(options=options)

url = "https://www.cathaybk.com.tw/cathaybk/"
driver.get(url)
driver.implicitly_wait(6)
driver.get_screenshot_as_file("cathaybk-1.png")
driver.implicitly_wait(6)
element=driver.find_element(By.CLASS_NAME,'cubre-a-burger__img')
driver.execute_script("arguments[0].click();",element)
time.sleep(1)

element1=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div')
driver.execute_script("arguments[0].click();",element1)
element2=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div')
driver.execute_script("arguments[0].click();",element2)
element3=driver.find_elements(By.XPATH,'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/*[@id="lnk_Link"]')
f.writelines('信用卡選單下面項目有{}個\n'.format(len(element3)))
print('信用卡選單下面項目有{}個'.format(len(element3)))
time.sleep(1)
driver.get_screenshot_as_file("cathaybk-2.png")

element4=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]')
driver.execute_script("arguments[0].click();",element4)
driver.implicitly_wait(6)
element5=driver.find_elements(By.XPATH,'/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/*')
f.writelines('(停發)信用卡數量{}個\n'.format(len(element5)))
print('(停發)信用卡數量{}個'.format(len(element5)))
element6=driver.find_element(By.XPATH,'/html/body/div/main/article/div/div/div/div[1]/div/div/a[6]')
driver.execute_script("arguments[0].click();",element6)
time.sleep(1)

element7=driver.find_element(By.XPATH,'/html/body/div/main/article/section[6]/div/div[2]')
#第一次不移動先截圖
driver.get_screenshot_as_file("cathaybk-credit_card-0.png")
Action = ActionChains(driver)
for i in range(1,len(element5)):#第一次已截圖，從1開始而非0
    Action.click_and_hold(element7).move_by_offset(-180,0).release().perform();
    time.sleep(1)
    driver.get_screenshot_as_file("cathaybk-credit_card-{}.png".format(i))
    time.sleep(1)

credit_card_screenshot_png=glob('cathaybk-credit_card-*.png')
f.writelines('截圖數量:{}\n'.format(len(credit_card_screenshot_png)))
print('截圖數量:{}'.format(len(credit_card_screenshot_png)))
if len(credit_card_screenshot_png)==len(element5):
    f.writelines('(停發)信用卡數量與截圖數量相同\n')
    print('(停發)信用卡數量與截圖數量相同')
else:
    f.writelines('(停發)信用卡數量與截圖數量不相同\n')
    print('(停發)信用卡數量與截圖數量不相同')
time.sleep(3)
f.close()
