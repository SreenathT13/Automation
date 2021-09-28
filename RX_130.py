from argparse import Action

import schedule
import time
import base64

import slider as slider
from PIL import Image
from webdriver_manager import driver
from selenium.webdriver import ActionChains

import RX130_config
from New_UI_Automation import Board_Automation, print_log, print_error, print_warning
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
board = Board_Automation("chrome")
board.open_browser()
board.list_boards()
board.click_cookies_ok()
board.connect_to_board('RX130')
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
time.sleep(10)


Right_to_Left = board.browser.find_element_by_xpath(RX130_config.RtoL).click()
print_log("water is injecting from right container to left container")

V_MAX = board.browser.find_element_by_xpath(RX130_config.Live_video).click()
time.sleep(10)
V_MIN = board.browser.find_element_by_xpath(RX130_config.Live_video).click()

Stop = board.browser.find_element_by_xpath(RX130_config.S_btn).click()
print_log("water injection stopped")

Graph_MAX = board.browser.find_element_by_xpath(RX130_config.G_btn).click()
time.sleep(10)
Graph_MIN = board.browser.find_element_by_xpath(RX130_config.G_btn).click()

Left_to_Right = board.browser.find_element_by_xpath(RX130_config.LtoR).click()
print_log("water is injecting from left container to right container")

V_MAX = board.browser.find_element_by_xpath(RX130_config.Live_video).click()

time.sleep(10)
V_MIN = board.browser.find_element_by_xpath(RX130_config.Live_video).click()

Stop = board.browser.find_element_by_xpath(RX130_config.S_btn).click()
print_log("water injection stopped")

Graph_MAX = board.browser.find_element_by_xpath(RX130_config.G_btn).click()
time.sleep(10)
Graph_MIN = board.browser.find_element_by_xpath(RX130_config.G_btn).click()
time.sleep(2)

Auto_mode = board.browser.find_element_by_xpath(RX130_config.A_btn).click()
print_log("auto injection mode is activated")
time.sleep(40)
Stop = board.browser.find_element_by_xpath(RX130_config.S_btn).click()
print_log("auto injection mode is stopped")
board.browser.implicitly_wait(10)

board.disconnect()
time.sleep(5)
board.close()
print(" last tested at :", print_log())
