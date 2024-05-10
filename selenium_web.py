# from selenium import webdriver
#
# class inflow():
#     def __init__(self):
#         self.driver = webdriver.Edge(executable_path="C:/Users/Paras/Downloads/Compressed/edgedriver_win64/msedgedriver.exe")

# from assistant import speak

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
class inflow():
    def __init__(self):
        # options = webdriver.EdgeOptions()
        # options.add_experimental_option("detach", False)
        service = Service("C:/Users/Paras/Downloads/Compressed/edgedriver_win64/msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        # self.driver = webdriver.Edge(service=service, options=options)

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        # old

        # search  =self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        # search.click()
        # search.send_keys(query)
        # enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        # enter.click()

        # new

        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')  # Use "find_element" with locator type
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()
        para1 = self.driver.find_element("xpath", '// *[ @ id = "mw-content-text"] / div[1] / p[1]')
        text = para1.text
        print(text)
        return text

# assist  = inflow()
# assist.get_info("neutron stars")






# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
#
# driver = webdriver.Edge(service=Service('C:/Users/Paras/Downloads/Compressed/edgedriver_win64/msedgedriver.exe'))
# driver.get('https://www.google.com')