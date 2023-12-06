from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from time import sleep

import time

def main():
  service = Service(ChromeDriverManager().install())
  navegador = webdriver.Chrome(service=service)
  
  navegador.maximize_window()

  
  login(navegador)
  searchTechRecruiters(navegador)
  
  
  
  
def login(navegador):
  navegador.get("https://www.linkedin.com/home")
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_key"]').send_keys('jgabfalcao@gmail.com') #Seu email
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_password"]').send_keys('batatinha') #Sua senha
  sleep(2)
  navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
  sleep(5)


def searchTechRecruiters(navegador):
  navegador.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106057199%22%5D&keywords=Tech%20Recruiter&origin=FACETED_SEARCH&sid=cE%40')
  sleep(5)
  
  elementos = navegador.find_elements(By.CSS_SELECTOR, 'li.reusable-search__result-container')
  
  for elemento in elementos:
    teste = elemento.find_element(By.CSS_SELECTOR, 'div.entity-result__actions entity-result__divider')
    print(len(teste))
    
if __name__ == "__main__":
   startTime = time.time()
   main()
   
   endTime = time.time()
   
   durationTime = endTime - startTime
   durationTime = round(durationTime, 2)
   
   print("Tempo de execução: ", durationTime, " segundos")