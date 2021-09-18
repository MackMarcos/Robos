from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

# Entrando no Chrome
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#contados da sua lista que deja mandar a menssagem
contatos = ['Bot_WhatsApp2' , 'Naj']

#mensagem a ser enviada
mensagem = 'Olá, foi um prazer te conhecer!'

#funções para buscar os contatos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    
    campo_mensagem[1].send_keys(mensagem)
    
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    
    enviar_mensagem(mensagem)
#campo de pesquisa
#<div role="textbox" class="_13NKt copyable-text selectable-text" 