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
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
    board.browser.implicitly_wait(3)

board.stream_check()

"""
Individual board functionality 
"""
#//*[@id="stepformcontainer"]/tx-elements[4]/div[2]/div/div/div/button/span
Transient_Response = '//*[@id="myTab"]/li[1]'
Transient_Response_APPLY = '//*[@id="stepformcontainer"]/tx-elements[4]/div[2]/div/div/div/button'
#disable = '//*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]/ng-content/tx-elements/div[2]/div/div[3]/plotly/div/div/div/svg[2]/g[3]/g[2]/g/g/g[2]/rect'

board.wait.until(EC.visibility_of_element_located((By.XPATH, Transient_Response_APPLY)))
board.browser.find_element_by_xpath(Transient_Response_APPLY).click()
# check transient response
start = time.time()
while 1:
    progress = board.read_progress()
    if progress:
        start = time.time()
    if "transient response evaluation is completed" in list(map(str.lower, progress)):
        print_log("Transient Response is working.")
        break
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
    board.browser.implicitly_wait(3)
# graph = '//*[@id="modebar-8795b9"]/div[1]/a/svg' //*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]
featureElement = board.browser.find_element_by_id("c8cadd6c-9093-54e0-2d14-26ea01cb4178")
featureElement_click = '//*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]/ng-content/tx-elements/div[2]/div/div[3]'
#disable = '//*[@id="c8cadd6c-9093-54e0-2d14-26ea01cb4178"]/ng-content/tx-elements/div[2]/div/div[3]/plotly/div/div/div/svg[2]/g[3]/g[2]/g/g/g[2]'

#board.browser.find_element_by_xpath(featureElement_click).click()
# location = featureElement.location

svg = featureElement.find_element_by_tag_name("svg")
size = svg.size
location = svg.location
board.browser.find_element_by_xpath(featureElement_click).location_once_scrolled_into_view
#time.sleep(10)
#board.browser.find_element_by_xpath(disable).click()
svg.screenshot("images/Transient_Response1.png")
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
