#Send automated whatsapp messages
from selenium import webdriver
from webzap import mandar_msg


#Abre o chrome e salva a uma variavel driver
driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)

#Abre a pagina do whatsapp
driver.get('https://web.whatsapp.com/')

#Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
names =  ['Tarefas', 'deutsch', 'Super Teste']
msg = 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários'

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')

mandar_msg(driver, names, msg, vezes=2)


    
