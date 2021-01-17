from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://lamp.ii.us.edu.pl/~mtdyd/zawody/')

#1 ---------------------2020----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2020')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg )

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#2 ---------------------2011----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2011')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg )

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#3 ---------------------2010_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2010')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#4 ---------------------2010_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2010')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#5 ---------------------2010_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2010')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#6 ---------------------2010----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2010')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#7 ---------------------2009_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2009')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#8 ---------------------2009_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2009')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#9 ---------------------2009_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2009')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#10 ---------------------2009----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2009')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

# 38---------------------2008_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2008')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#11 ---------------------2008_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2008')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#12 ---------------------2008_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2008')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#13 ---------------------2008----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2008')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#14 ---------------------2007_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2007')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#15 ---------------------2007_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2007')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#16 ---------------------2007_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2007')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#17 ---------------------2007----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2007')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#18 ---------------------2006_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2006')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#19 ---------------------2006_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2006')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#20 ---------------------2006_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2006')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#21 ---------------------2006----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2006')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#22 ---------------------2003_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2003')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#23 ---------------------2003_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2003')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#24 ---------------------2003_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2003')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#25 ---------------------2003----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2003')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#26 ---------------------2002_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2002')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#27 ---------------------2002_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2002')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#28 ---------------------2002_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2002')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#29 ---------------------2002----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-2002')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#30 ---------------------1956_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1956')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#31 ---------------------1956_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1956')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#32 ---------------------1956_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1956')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#33 ---------------------1956----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1956')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#34 ---------------------1955_zgoda_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1955')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#35 ---------------------1955_zaswiadczenie----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1955')

def zaznacz_zaswiadczenie(driver):
    zaswiadczenie = driver.find_element_by_xpath('//*[@id="lekarz"]')
    zaswiadczenie.click()

zaznacz_zaswiadczenie(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#36 ---------------------1955_zgoda----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1955')

def zaznacz_zgoda(driver):
    zgoda = driver.find_element_by_xpath('//*[@id="rodzice"]')
    zgoda.click()

zaznacz_zgoda(driver)

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#37 ---------------------1955----------------------
search_input_first_name = driver.find_element_by_xpath('//*[@id="inputEmail3"]')
search_input_first_name.send_keys('Marcin')

search_input_last_name = driver.find_element_by_xpath('//*[@id="inputPassword3"]')
search_input_last_name.send_keys('Kowal')

search_input_date = driver.find_element_by_xpath('//*[@id="dataU"]')
search_input_date.send_keys('01-01-1955')

time.sleep(2)
def wyslij(driver):
    wysylanie = driver.find_element_by_xpath('//*[@id="formma"]/div[6]/div/button')
    wysylanie.click()

wyslij(driver)

obj = driver.switch_to.alert

obj.accept()

msg=obj.text
print ("Stan: " + msg)

time.sleep(2)

obj.accept()

# refresh przegladarki
driver.refresh()

#quit
driver.quit()