from time import sleep

from selenium import  webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


class music:
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        service = Service("C:/Users/Paras/Downloads/Compressed/edgedriver_win64/msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)

    def play(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        # video  = self.driver.find_element('xpath','//*[@id="video-title"]/yt-formatted-string/span')
        video  = self.driver.find_element('xpath','//*[@id="video-title"]')
        video.click()
        sleep(1000000)

# assist = music()
# assist.play("the night we met")

