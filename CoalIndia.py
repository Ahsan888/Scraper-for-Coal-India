import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.options
import time
import os
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium.webdriver.support.ui import Select
from os import listdir
from os.path import isfile, join
import shutil

ocmpath=r"C:\Users\Lenovo\Downloads\OCM"
mixpath=r"C:\Users\Lenovo\Downloads\MIX"
ugpath=r"C:\Users\Lenovo\Downloads\UG"

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-user-media-security=true")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(PATH, options=options)
driver.get("http://apps.coalindia.in:8080/apex/f?p=139:51:9336877033989::NO:::")
time.sleep(20)
driver.find_element_by_xpath("//*[contains(text(), 'list date wise pod')]").click()
driver.maximize_window()
select = Select(driver.find_element_by_id('P51_SUB_CODE'))
options1=select.options
for i in range(1,len(options1)):
    try:
        select = Select(driver.find_element_by_id('P51_SUB_CODE'))
        options1 = select.options
        try:
            select.select_by_index(i)

        except:
            pass
        try:
            obj = driver.switch_to.alert
            obj.accept()
        except:
            pass
        time.sleep(2)
        select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
        options2=select2.options
        for a in range(1,len(options2)):
            select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
            options2 = select2.options

            try:
                select2.select_by_visible_text("OCM")
                try:
                    obj = driver.switch_to.alert
                    obj.accept()
                except:
                    pass
                select3 = Select(driver.find_element_by_id('P51_UNIT'))
                options3 = select3.options
                for g in range(1, len(options3)):
                    try:
                        select3 = Select(driver.find_element_by_id('P51_UNIT'))
                        options3 = select3.options
                        select3.select_by_index(g)
                    except:
                        pass
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    driver.find_element_by_id("P51_YEAR_0").click()
                    print("selected 2019")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))

                        print(data11)
                        shutil.move(data11[0], ocmpath)
                    except:
                        pass



                    driver.find_element_by_id("P51_YEAR_1").click()
                    print("selected 2020")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))

                        print(data11)
                        shutil.move(data11[0], ocmpath)
                    except:
                        pass

            except:
                pass


        select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
        options2 = select2.options
        for a in range(1, len(options2)):
            select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
            options2 = select2.options
            try:
                select2.select_by_visible_text("UG")
                try:
                    obj = driver.switch_to.alert
                    obj.accept()
                except:
                    pass
                select3 = Select(driver.find_element_by_id('P51_UNIT'))
                options3 = select3.options
                for g in range(1, len(options3)):
                    try:
                        select3 = Select(driver.find_element_by_id('P51_UNIT'))
                        options3 = select3.options
                        select3.select_by_index(g)
                    except:
                        pass
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    driver.find_element_by_id("P51_YEAR_0").click()
                    print("selected 2019")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))
                        shutil.move(data11[0], ugpath)
                    except:
                        pass
                    driver.find_element_by_id("P51_YEAR_1").click()
                    print("selected 2020")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))
                        shutil.move(data11[0], ugpath)
                    except:
                        pass
            except:
                pass
        select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
        options2 = select2.options
        for a in range(1, len(options2)):
            select2 = Select(driver.find_element_by_id('P51_UNIT_TYPE'))
            options2 = select2.options
            try:
                select2.select_by_visible_text("MIX")
                try:
                    obj = driver.switch_to.alert
                    obj.accept()
                except:
                    pass
                select3 = Select(driver.find_element_by_id('P51_UNIT'))
                options3 = select3.options
                for g in range(1, len(options3)):
                    try:
                        select3 = Select(driver.find_element_by_id('P51_UNIT'))
                        options3 = select3.options
                        select3.select_by_index(g)
                    except:
                        pass
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    driver.find_element_by_id("P51_YEAR_0").click()
                    print("selected 2019")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))
                        shutil.move(data11[0], mixpath)
                    except:
                        pass
                    driver.find_element_by_id("P51_YEAR_1").click()
                    print("selected 2020")
                    try:
                        obj = driver.switch_to.alert
                        obj.accept()
                    except:
                        pass
                    try:
                        driver.find_element_by_xpath("//*[contains(text(), 'Download')]").click()
                        time.sleep(5)
                        for path, subdirs, files in os.walk(r"C:\d"):
                            for file in files:
                                data11.append(os.path.join(path, file))
                        shutil.move(data11[0], ugpath)
                    except:
                        pass
            except:
                pass
    except:
        pass
