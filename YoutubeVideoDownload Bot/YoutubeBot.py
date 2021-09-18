from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

# link_youtube = str(input('Digite o link: '))

link_youtube = str(input('Digite o link:'))

driver = webdriver.Chrome()

driver.get('https://pt.savefrom.net/15/')


campo_link = driver.find_element_by_id("sf_url")
campo_link.send_keys(link_youtube)
campo_link.send_keys(Keys.ENTER)

time.sleep(5)


campo_mp4 = driver.find_element_by_class_name("def-btn-box")
campo_mp4.click()



