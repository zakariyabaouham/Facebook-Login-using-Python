from selenium import webdriver 
from time import sleep 
  
usr=input('Tapez votre Email Id:')  
pwd=input('Tapez votre Password:')  

driver = webdriver.Chrome() 
driver.get('https://www.facebook.com/') 
print ("Facebook Ouvert!!") 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entré!!") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entré!!") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("C fait") 
input("Appuyez sur n'importe quoi pour quitter") 
driver.quit() 
print("Terminé")
