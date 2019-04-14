#Send automated whatsapp messages
from selenium import webdriver

#Abre o chrome e salva a uma variavel driver
driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)

#Abre a pagina do whatsapp
driver.get('https://web.whatsapp.com/')

#Recebe o nome do usuário/grupo para quem as mensagens serão mandadas assim como a mensagem a ser mandada
name =  'Tarefas'
msg = 'Parabens você foi hackeado!'

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')

#Encontra o usuário colocado em name e clica nele
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

#Encontra a caixa de mensagem e escreve a msg nela
msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')
msg_box.send_keys(msg)

#Encontra o botão de enviar e clica nele
button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
button.click()
