from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from time import sleep

service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

navegador.get("https://www.linkedin.com/home")

sleep(2)

navegador.find_element('xpath', '//*[@id="session_key"]').send_keys('') #Seu email

sleep(2)

navegador.find_element('xpath', '//*[@id="session_password"]').send_keys('') #Sua senha

sleep(2)

navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()

sleep(5)

