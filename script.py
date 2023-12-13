from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from time import sleep

import time

def main():
  service = Service(ChromeDriverManager().install())
  navegador = webdriver.Chrome(service=service)
  
  navegador.maximize_window()

  
  # login(navegador)
  # searchTechRecruiters(navegador)
  
  navegador.get("https://www.linkedin.com/home")
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_key"]').send_keys('') #Seu email
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_password"]').send_keys('') #Sua senha
  sleep(2)
  navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
  sleep(5)
  
  navegador.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106057199%22%5D&keywords=Tech%20Recruiter&origin=FACETED_SEARCH&sid=cE%40')
  sleep(10)
  
  divElements = navegador.find_elements(By.CLASS_NAME ,'reusable-search__result-container')
  
  for elemento in divElements:
    profileStatus = elemento.find_element(By.CLASS_NAME, 'artdeco-button__text')
    print(profileStatus.text)
     
    if(profileStatus.text == "Conectar"):
      profileDiv = elemento.find_element(By.CLASS_NAME, 'entity-result__actions')
      if(profileDiv):
        profileButton = profileDiv.find_element(By.TAG_NAME, 'button')
        if(profileButton):
          profileButton.click()
          sleep(5)
          popUpRequest = navegador.find_element(By.CSS_SELECTOR, 'button[aria-label="Enviar agora"]')
          if(popUpRequest):
            popUpRequest.click()
          else:
            print("Não encontrou o botão de PopUp")  
        else:
          print("Não encontrou o botão")
      else:
        print("Não encontrou a div")
      # profileButton.click()
  
  sleep(500)   
      

  
  # html = navegador.page_source
  
  # teste = BeautifulSoup(html, 'html.parser')
  
  # teste2 = teste.find('ul', attrs={'class': 'reusable-search__entity-result-list list-style-none'}).find_all('li')
  
  # print(teste2)
  
  
  # elementos = navegador.find_elements(By.CSS_SELECTOR, 'li.reusable-search__result-container')
  
  # print(len(elementos))
    
if __name__ == "__main__":
   startTime = time.time()
   main()
   
   endTime = time.time()
   
   durationTime = endTime - startTime
   durationTime = round(durationTime, 2)
   
   print("Tempo de execução: ", durationTime, " segundos")