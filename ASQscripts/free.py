from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


while True:

        
	driver = webdriver.Firefox()

	driver.get('https://campusonline.uni-ulm.de/CoronaNG/index.html')


	name = driver.find_element_by_name("uid")

	name.send_keys('USERNAME')

	pw = driver.find_element_by_name("password")
	pw.send_keys('PASSWORT')

	button = driver.find_element_by_css_selector('[value="Anmelden"]')
	button.click()

	viewed = driver.find_element_by_css_selector('[href="/CoronaNG/user/mycorona.html"]')
	viewed.click()

	driver.find_element_by_css_selector('[value="Ausführen"]').click()

	select = Select(driver.find_element_by_name('action'))
	select.select_by_visible_text('An Markierten teilnehmen')

	driver.find_element_by_css_selector('[value="Ausführen"]').click()
	time.sleep(4)
	driver.quit()
	time.sleep(62)

