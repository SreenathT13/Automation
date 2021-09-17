import base64
from PIL import Image
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
while 1:
    progress = board.read_progress()
    if progress:
        start = time.time()
    if "system ready" in list(map(str.lower, progress)):
        print_log("System is ready")
        break
    if time.time() - start > 120:
        print_error("progress is not active ")

        board.close()
        exit(0)
    board.browser.implicitly_wait(3)

board.stream_check()
video_response ='//*[@id="video-live"]'
board.browser.find_element_by_xpath(video_response).click()
board.browser.maximize_window()
""" 
Individual board functionality 
"""
#//*[@id="stepformcontainer"]/tx-elements[4]/div[2]/div/div/div/button/span
#------ Transient Response ---------
Startup_Response = '//*[@id="myTab"]/li[3]'
Startup_Response_APPLY = '//*[@id="stepformcontainer"]/tx-elements[3]/div[2]/div/div/div/button'
board.browser.find_element_by_xpath(Startup_Response).click()
board.wait.until(EC.visibility_of_element_located((By.XPATH, Startup_Response_APPLY)))
board.browser.find_element_by_xpath(Startup_Response_APPLY).click()
# check transient response
start = time.time()
flag = 1
while flag:
    progress = board.read_progress()
    if progress:
        start = time.time()

    for i in progress:
        if "Start-up response evalaution is completed" in i:
            print("Start-up Response is working")
            flag = 0
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")

        board.close()
        exit(0)
    board.browser.implicitly_wait(3)



featureElement = board.browser.find_element_by_id("c8cadd6c-9093-54e0-2d14-26ea01cb4178")
featureElement_click = '//*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]/ng-content/tx-elements/div[2]/div/div[3]'
svg = featureElement.find_element_by_tag_name("svg")
size = svg.size
location = svg.location
board.browser.find_element_by_xpath(featureElement_click).location_once_scrolled_into_view
svg.screenshot(r"images/Start-up_Response1.png")
#board.browser.save_screenshot("fullPageScreenshot2.png")

board.browser.implicitly_wait(10)
board.disconnect()
time.sleep(5)
board.close()

















































# graph = '//*[@id="modebar-8795b9"]/div[1]/a/svg' //*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]
# location = featureElement.location







# board.browser.save_screenshot ("fullPageScreenshot.png")
# x = location['x']
# y = location['y']
# w = x + size['width']
# h = y + size['height']
# fullImg = Image.open("fullPageScreenshot.png")
# cropImg = fullImg.crop((x, y, w, h))
 #cropImg.save("cropImage.png")
