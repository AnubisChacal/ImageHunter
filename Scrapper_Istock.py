# Importe das bibliotecas 
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#=================================================================
# Configurações do Selenium
# Caso mude de web-drive sera necessario auterar essa região
# Recomendo utlixar o firefox por motivos de bypass de aspectos de segurança

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("general.useragent.override", user_agent)

driver = webdriver.Firefox(executable_path='C:\\Users\\Gabri\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.11\\geckodriver.exe')
#======================================================================
url = 'https://www.istockphoto.com/'  
driver.get(url) # Abra a página da web com o Selenium
#========================================================================
# Realize a pesquisa
get = driver.find_element(By.XPATH, '//*[@id="hero--free-trial"]/div[1]/div/div/div/div/div/div/div[1]/div[1]/form/input')
pesquisa = 'superman'  # Substitua com a pesquisa desejada
get.send_keys(get)
time.sleep(2)
get.send_keys(Keys.ENTER)
time.sleep(2)
#===============================================================================================
# Função para extrair imagens da página de pesquisa
# Ele ta fazendo um find na class que determina o bloco das imagems e depois fazendo um find na class da galeria de imagens
def download_imagens(driver ):
    # Encontre o elemento geral
    container_element = driver.find_element(By.CLASS_NAME, "DE6jTiCmOG8IPNVbM7pJ")
    # Encontre todos os elementos class da galeria
    img_elements = container_element.find_elements(By.CLASS_NAME, "yGh0CfFS4AMLWjEE9W7v")
#===============================================================================================
    #cria diretorio com base na pesquisa
    download_directory = f"{pesquisa}"
    os.makedirs(download_directory, exist_ok=True)
#===============================================================================================
    # Contador para nomear as imagens
    image_count = 1
    
    for link_element in img_elements:
        img_url = link_element.get_attribute("src")
        
        # Faça o download da imagem
        if img_url:
            response = requests.get(img_url)
            
            # Verifique se a resposta foi bem-sucedida
            if response.status_code == 200:
                # Especifique o diretório para salvar as imagens (modifique conforme necessário)
                filename = f"{download_directory}/imagem_{image_count}.jpg"
                
                
                # Salve a imagem no disco
                with open(filename, "wb") as file:
                    file.write(response.content)
                
                image_count += 1
            else:
                print(f"Erro ao baixar a imagem de {img_url}")
#===============================================================================================
# Chamando a função para baixar imagens
download_imagens(driver,)    