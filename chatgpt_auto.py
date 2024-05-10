# from time import sleep

# from selenium import webdriver
# from selenium.webdriver.edge.options import Options
# from selenium.webdriver.edge.service import Service

# counter = 3
# class chat():
#     def __init__(self):
#         # options = webdriver.EdgeOptions()
#         # options.add_experimental_option("detach", False)
#         service = Service("C:/Users/Paras/Downloads/Compressed/edgedriver_win64/msedgedriver.exe")
#         self.driver = webdriver.Edge(service=service)
#         # self.driver = webdriver.Edge(service=service, options=options)

#     def get_answer(self, query, counter1):
#         self.query = query
#         self.driver.get(url="https://chatgpt.com/")

#         # new

#         # new_chat = self.driver.find_element("xpath", '//*[@id="__next"]/div[1]/div[1]/div/div/div/div/nav/div[1]/div[1]/div/a')  # Use "find_element" with locator type
#         # new_chat.click()
#         # print("new_chat")
#         # sleep(100000)
#         # ask = self.driver.find_element("xpath",'//*[@id="prompt-textarea"]')
#         # ask.click()
#         # print("search")
#         # ask.send_keys(query)
#         # print("query sent")
#         # enter = self.driver.find_element("xpath", '//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[2]/div[1]/div/form/div/div[2]/div/button')
#         # enter.click()
#         # print("send clicked")
#         # para2 = self.driver.find_element("xpath", f'//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[{counter1}]/div/div/div[2]/div[2]/div[1]/div')
#         # print("para data stored")
#         # counter1 = counter1 + 2
#         # answer = para2.text
#         # print("para data extracted")
#         # print(answer)
#         # return answer

# chatgpt  = chat()
# chatgpt.get_answer("neutron stars",counter)


# import pyautogui
import time  # Import the time module for waiting
# import path

# edge = 'C:\\Users\\Paras\\Desktop\\Assistant\\images\\edge.png'
# new_chat = 'C:\\Users\\Paras\\Desktop\\Assistant\\images\\new_chat.png'
#
# # Get the position of the Microsoft Edge shortcut
# edge_shortcut = pyautogui.locateOnScreen(edge)
# new_chat = pyautogui.locateOnScreen(new_chat)
#
# # Check if images are found
# if edge_shortcut is not None and new_chat is not None:
#     # Click on the Microsoft Edge shortcut
#     pyautogui.click(edge_shortcut)
#
#     # Wait for Microsoft Edge to open
#     time.sleep(5)  # Use time.sleep() instead of pyautogui.wait() for longer waits
#
#     # Press the F11 key to open Microsoft Edge in fullscreen
#     pyautogui.hotkey('f11')
#
#     # Click on the "New Chat" button
#     pyautogui.click(new_chat)
# else:
#     print("Images not found. Check the path and ensure the images exist.")

