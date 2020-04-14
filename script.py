from selenium import webdriver
from colored import fg,attr
from time import sleep
color1 = fg('#e74c3c')
color2 = fg('#27ae60')
print(color1+'''
-------------------------------------------------
-- INSTAGRAM AUTO VIEWER UNLIMITED 50 EVERY 1M --
-------------------------------------------------
-- >> CODED BY : ABDELRAHMAN ABOULDAHAB        --
-- >> GITHUB   : rootxnova                     --
-- >> FACEBOOK : AbdelrahmanAbouldahabOfficial --
-- >> INSTA    : 300bad                        --
-- >> EMAIL    : rootxnova@mail.ru             --
-------------------------------------------------
''')
video = input('Enter Video Link : ')
driver = webdriver.Chrome()
a = 0
while a < 1:
	driver.get('https://igtools.net/video')
	link = driver.find_element_by_xpath('//*[@id="media_form"]/div/input').click()
	link = driver.find_element_by_xpath('//*[@id="media_form"]/div/input')
	link.send_keys(video)
	gooo = driver.find_element_by_xpath('//*[@id="media_form"]/button').click()
	cler = driver.find_element_by_xpath('//*[@id="form"]/div[2]/input').click()
	cler = driver.find_element_by_xpath('//*[@id="form"]/div[2]/input').clear()
	cler.send_keys('50')
	done = driver.find_element_by_xpath('//*[@id="submit"]').click()
	print(color2+'-----[ ^_ VIEWS SENT SUCCESSFULY _^ ]-----')
	sleep(70)
