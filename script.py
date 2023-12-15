from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

import time

def main():
  service = Service(ChromeDriverManager().install())
  navegador = webdriver.Chrome(service=service)
  
  navegador.maximize_window()
  
  navegador.get("https://www.linkedin.com/home")
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_key"]').send_keys('') #Seu email
  sleep(2)
  navegador.find_element('xpath', '//*[@id="session_password"]').send_keys('') #Sua senha
  sleep(2)
  navegador.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
  sleep(5)    
  
  tempo_limite = 10
  tempo_limite_pop_UP = 1
  
  for page in range(1,11):
    navegador.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106057199%22%5D&keywords=Tech%20Recruiter&origin=FACETED_SEARCH&page=' + str(page) + '&sid=cE%40')
    
    WebDriverWait(navegador, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'reusable-search__result-container')))
  
    divElements = navegador.find_elements(By.CLASS_NAME ,'reusable-search__result-container')
  
    for elemento in divElements:
      WebDriverWait(elemento, tempo_limite).until(EC.visibility_of_element_located((By.CLASS_NAME, 'artdeco-button__text')))
      
      profileStatus = elemento.find_element(By.CLASS_NAME, 'artdeco-button__text')
      print(profileStatus.text)
     
      if(profileStatus.text == "Conectar"):
        profileDiv = elemento.find_element(By.CLASS_NAME, 'entity-result__actions')
        if(profileDiv):
          profileButton = profileDiv.find_element(By.TAG_NAME, 'button')
          if(profileButton):
            profileButton.click()
            sleep(0.5)
            try:
              WebDriverWait(navegador, tempo_limite_pop_UP).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="email"]')))
              popUp = navegador.find_element(By.CSS_SELECTOR, 'label[for="email"]')
              popUpText = popUp.text
              
              print(popUpText)
              
              if(popUpText == "Para confirmar que este usuário é seu conhecido, insira o endereço de e-mail do mesmo para se conectar. Você também pode incluir uma nota pessoal. Saiba mais"):
                popUpClose = navegador.find_element(By.CSS_SELECTOR, 'button[aria-label="Fechar"]')
                popUpClose.click()
                
                continue
            except:
              print("Pop-up negativo não encontrado")

            popUpRequest = navegador.find_element(By.CSS_SELECTOR, 'button[aria-label="Enviar agora"]')
            if(popUpRequest):
              popUpRequest.click()
            else:
              print("Não encontrou o botão de PopUp")  
            
          else:
            print("Não encontrou o botão")
        else:
          print("Não encontrou a div") 
      else: 
        print("Não é possível conectar")
  
  
if __name__ == "__main__":
   startTime = time.time()
   main()
   
   endTime = time.time()
   
   durationTime = endTime - startTime
   durationTime = round(durationTime, 2)
   
   print("Tempo de execução: ", durationTime, " segundos")