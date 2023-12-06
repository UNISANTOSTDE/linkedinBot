from selenium import webdriver

import time

class CookieClicker:
  def __init__(self):
    self.link = "https://orteil.dashnet.org/cookieclicker/"
    self.site_map = {}
    
    self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    self.driver.maximize_window() 