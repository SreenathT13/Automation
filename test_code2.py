import schedule
import time
import base64
from PIL import Image
from webdriver_manager import driver

from OLD_UI_Automation import Board_Automation, print_log, print_error, print_warning
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
board = Board_Automation("chrome")
board.open_browser()
board.list_boards()
board.click_cookies_ok()
board.connect_to_board('ISL81802')
start = time.time()
#schedule.every(10).minutes.do()
while 1:
    progress = board.read_progress()
    if progress:
        start = time.time()
    if "system ready" in list(map(str.lower, progress)):
        print_log("System is ready")
        break
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
    board.browser.implicitly_wait(3)

board.stream_check()

"""
Individual board functionality 
"""
#//*[@id="stepformcontainer"]/tx-elements[4]/div[2]/div/div/div/button/span
Load_Regulation = '//*[@id="myTab"]/li[2]'
Load_Regulation_APPLY = '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div/div[1]/div/div/div/div/div/ul/li[1]/div/div/tx-elements/div[2]/div/div/ng-content[2]/ng-content/tx-elements/div[2]/div/div/form/tx-elements[4]/div[2]/div/div/div/button'
board.browser.find_element_by_xpath(Load_Regulation).click()
#time.sleep(2)
#board.browser.switch_to.frame(Load_Regulation)
#time.sleep(2)
#board.browser.find_element_by_css_selector(Load_Regulation_APPLY).location_once_scrolled_into_view
board.wait.until(EC.visibility_of_element_located((By.XPATH, Load_Regulation_APPLY)))
board.browser.find_element_by_xpath(Load_Regulation_APPLY).click()
# check Load Regulation
start = time.time()
flag =1
while flag:
    progress = board.read_progress()
    if progress:
        start = time.time()
    for i in progress:
        if "Load regulation evaluation is completed" in i:
            print_log("Load Regulation is working.")
            flag = 0
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
    board.browser.implicitly_wait(3)
# graph = '//*[@id="modebar-8795b9"]/div[1]/a/svg' //*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]
featureElement = board.browser.find_element_by_id("c8cadd6c-9093-54e0-2d14-26ea01cb4178")

featureElement_click = '//*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]/ng-content/tx-elements/div[2]/div/div[3]'
# location = featureElement.location
svg = featureElement.find_element_by_tag_name("svg")
size = svg.size
location = svg.location
board.browser.find_element_by_xpath(featureElement_click).location_once_scrolled_into_view
svg.screenshot("images/Load_Regulation.png")
# board.browser.save_screenshot ("fullPageScreenshot.png")
# x = location['x']
# y = location['y']
# w = x + size['width']
# h = y + size['height']
# fullImg = Image.open("fullPageScreenshot.png")
# cropImg = fullImg.crop((x, y, w, h))
# cropImg.save("cropImage.png")

board.browser.implicitly_wait(10)
board.disconnect()
time.sleep(5)
board.close()
