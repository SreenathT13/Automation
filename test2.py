from selenium.webdriver import ActionChains

import NEW_config
from New_UI_Automation import Board_Automation, print_log, print_error, print_warning


import time
board = Board_Automation("chrome")
board.open_browser()
board.list_boards()
board.click_cookies_ok()
board.connect_to_board('CN251')
start = time.time()


flag = 1
while flag:
    progress = board.read_progress()
    if progress:
        start = time.time()
    for i in progress:
        if "SYSTEM READY" in i:
            print_log("System is Ready")
            flag = 0
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
board.browser.implicitly_wait(3)

board.stream_check()




zoom_slider = board.browser.find_element_by_xpath(NEW_config.zoom)
light_slider = board.browser.find_element_by_xpath(NEW_config.light)

ActionChains(board.browser).move_to_element(light_slider).\
    click_and_hold(light_slider).pause(2).move_by_offset(-100, 100).release().perform()
light_button = board.browser.find_element_by_xpath(NEW_config.light_set).click()
time.sleep(5)
ActionChains(board.browser).move_to_element(zoom_slider).\
    click_and_hold(zoom_slider).pause(2).move_by_offset(130, 0).release().perform()
zoom_button = board.browser.find_element_by_xpath(NEW_config.zoom_set).click()
time.sleep(10)
flag = 1
while flag:
    progress = board.read_progress()
    if progress:
        start = time.time()
    for i in progress:
        if " Zooming completed" in i:
            print_log("Light Intensity at 0% & Zoom at 100% is working")
            flag = 0
    if time.time() - start > 120:
        print_error("progress is not active for 2 min")
        board.close()
        exit(0)
    board.browser.implicitly_wait(3)



video = board.browser.find_element_by_xpath(NEW_config.VIDEO)

size = video.size
location = video.location

video.screenshot("images/l_0%&z_100%_screenshot.png")


board.browser.implicitly_wait(10)
board.disconnect()
time.sleep(5)
board.close()
