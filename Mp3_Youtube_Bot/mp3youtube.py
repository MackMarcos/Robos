from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

# link_youtube = str(input('Digite o link: '))

link_youtube = str(input('Digite o link:'))

driver = webdriver.Chrome()

driver.get('https://www.snappea.com/pt/')

campo_link = driver.find_element_by_id('searchContent')
campo_link.send_keys(link_youtube)
campo_link.send_keys(Keys.ENTER)

time.sleep(5)

campo_mp3 = driver.find_elements_by_xpath("//div[contains(@class,'_1lg94e4')]")
#campo_mp3.click()
campo_mp3[3].click()