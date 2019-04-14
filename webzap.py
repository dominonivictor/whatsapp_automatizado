#Organizando o código
from selenium import webdriver
from time import sleep

def fazer_decisao(names, msg, vezes=1):
    decisao = ''
    #Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
    print('Deseja alterar os contatos? (s/n) \nContatos atualmente: {}'.format(', '.join(names)))
    decisao = input().lower()
    if decisao == 's':
        names = input('''Insira os nomes dos contatos EXATAMENTE como estão no seu Whatsapp
                         separados APENAS por virgula. ex: Joao Pedro,Maria,Jose \n''').split(',')
    decisao = ''   
    #Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
    print('Deseja alterar a mensagem? (s/n) \nMensagem atual: {}'.format(msg))
    decisao = input().lower()    
    if decisao == 's':
        msg = input('Insira a mensagem que deseja mandar para os contatos escolhidos \n')
    decisao = '' 
    #Recebe o numero de vezes que o usuário deseja mandar a mensagem        
    print('Deseja alterar o numero de vezes? (s/n) \nNúmero de vezes atual: {}'.format(vezes))
    decisao = input().lower()
    if decisao == 's':
        vezes = int(input('Insira o numero de vezes que deseja mandar a mensagem: \n'))
    decisao = ''
    
    
    return (names, msg, vezes)

#função para mandar 1 mensagem para diversos usuários 1 vez, com opção de aumentar o numero de mensagens, retorna os novos valores de contatos, msgs e vezes
def mandar_msg(driver, names, msg, vezes=1):

    names, msg, vezes = fazer_decisao(names, msg, vezes)
    #Aqui itera pela lista de nomes chamando cada item da iteração de nome
    for name in names:
        #Encontra o usuário colocado em name e clica nele
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        
        for i in range(vezes):
            #Encontra a caixa de mensagem e escreve a msg nela
            msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')
            msg_box.send_keys(msg)

            #Encontra o botão de enviar e clica nele
            button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
            button.click()
            
        #Espera 0.1 segundos antes de passar para a próxima etapa, pois ocorreu um bug ao tentar clicar em uma mensagem
        #para outros usuarios quase ao mesmo tempo que estavam digitando e enviando a mensagem
        sleep(0.1)
    
    return names, msg, vezes
        
def abre_driver():
    #Abre o chrome e salva a uma variavel driver
    driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
    driver = webdriver.Chrome(driverPath)

    #Abre a pagina do whatsapp
    driver.get('https://web.whatsapp.com/')
    return driver
    