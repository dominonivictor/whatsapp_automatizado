#Send automated whatsapp messages
from selenium import webdriver
from time import sleep

#Abre o chrome e salva a uma variavel driver
driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)

#Abre a pagina do whatsapp
driver.get('https://web.whatsapp.com/')

#Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
names =  ['Tarefas', 'deutsch', 'Super Teste', 'Mini Sch@tli SP']
msg = 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários'

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')

#Aqui itera pela lista de nomes chamando cada item da iteração de nome
for name in names:
    #Encontra o usuário colocado em name e clica nele
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    #Encontra a caixa de mensagem e escreve a msg nela
    msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')
    msg_box.send_keys(msg)

    #Encontra o botão de enviar e clica nele
    button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
    button.click()
    
    #Espera 0.5 segundos antes de passar para a próxima etapa, pois ocorreu um bug ao tentar clicar em uma mensagem
    #para outros usuarios quase ao mesmo tempo que estavam digitando e enviando a mensagem
    sleep(0.5)
