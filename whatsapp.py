#Send automated whatsapp messages
from selenium import webdriver

driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get('https://web.whatsapp.com/')
name =  'Tarefas'
msg = 'Parabens você foi hackeado!'

input('Pressione qualquer tecla após o scan')

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

for i in range(10): #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
    button.click()
   
