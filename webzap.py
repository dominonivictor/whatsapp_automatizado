#Organizando o código
from selenium import webdriver
from time import sleep

def fazer_decisao(nomes, msg, vezes=1):
    '''
    Recebe os nomes salvos nas últimas sessões (na 1a iteração usa as constantes inicializadas) e recebe do usuario novas opções caso ele queira 
    '''

    decisao = ''
    #Recebe o nome dos usuários/grupos para quem a mensagem será enviada
    print('Deseja alterar os contatos que enviará a mensagem? (s/n) \nContatos: {}'.format(', '.join(nomes)))
    decisao = input().lower()
    if decisao == 's':
        nomes = input('''Insira os nomes dos contatos EXATAMENTE como estão no seu Whatsapp separados APENAS por virgula.\nex: Joao Pedro,Maria,Jose A. Fut\n''').split(',')
    decisao = ''   
    #Recebe a mensagem que será enviada
    print('Deseja alterar a mensagem? (s/n) \nMensagem atual: {}'.format(msg))
    decisao = input().lower()    
    if decisao == 's':
        msg = input('Insira a mensagem que deseja mandar para os contatos escolhidos \n')
    decisao = '' 
    #Recebe o numero de vezes que o usuário deseja mandar a mensagem        
    print('Deseja alterar o numero de vezes que enviará a mensagem? (s/n) \nNúmero de vezes atual: {}'.format(vezes))
    decisao = input().lower()
    if decisao == 's':
        vezes = int(input('Insira o numero de vezes que deseja mandar a mensagem: \n'))
    decisao = ''
    
    
    return (nomes, msg, vezes)

#função para mandar 1 mensagem para diversos usuários 1 vez, com opção de aumentar 
#o numero de mensagens, retorna os novos valores de contatos, msgs e vezes para serem
#salvos para a próxima iteração
def mandar_msg(driver, nomes, msg, vezes=1):

    nomes, msg, vezes = fazer_decisao(nomes, msg, vezes)
    #Aqui itera pela lista de nomes chamando cada item da iteração de nome
    for nome in nomes:
        #Encontra o usuário colocado em nome, salva em uma variável e clica nele
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(nome))
        user.click()
        
        #para o numero na variavel vezes de iterações
        for i in range(vezes):
            #Encontra a caixa de mensagem, salva em uma variável e escreve a msg nela
            msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')
            msg_box.send_keys(msg)

            #Encontra o botão de enviar, salva em uma variável e clica nele
            button = driver.find_element_by_xpath('//button[@class = "_35EW6"]')
            button.click()
            
        #Espera 0.1 segundos antes de passar para a próxima etapa, pois ocorreu um bug ao tentar clicar em uma mensagem
        #para outros usuarios quase ao mesmo tempo que estavam digitando e enviando a mensagem, futuramente melhorarei 
        #essa parte com algo que reconheça quando está pronto para continuar sem ocorrer o bug
        sleep(0.1)
    
    return nomes, msg, vezes
        
def abre_driver():
    #Abre o chrome e salva a uma variavel driver
    driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
    driver = webdriver.Chrome(driverPath)

    #Abre a pagina do whatsapp
    driver.get('https://web.whatsapp.com/')
    return driver
 

#Esta bugado ainda pois nao detecta contatos em grupos que o usuario nao é administrador 
def contatos_grupo(driver, grupo='Musicas pro Mundo Ouvir'):
    decisao = ''
    print('Deseja ver os contatos de um grupo que você é administrador?(s/n)')
    decisao = input().lower()
    
    if decisao == 'n': return False
    
    print('Deseja alterar os contatos do grupo selecionado?(s/n) \n Grupo: {}'.format(grupo))
    decisao = input().lower()
    
    if decisao == 's': grupo = input('Insira o nome do grupo: ')
    
    #Essa versão só funciona para grupos que o usuário é administrador do grupo
    contatos = []
    
    #Encontra o usuário colocado em grupo e clica nele
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(grupo))
    user.click()
    #Clica na aba superiro, mas talvez nem seja necessário
    abaSuperior = driver.find_element_by_xpath('//div[@class="_5SiUq"]')
    abaSuperior.click()
    
    caminho = driver.find_elements_by_xpath('//div[@class="_2EXPL _3xj48"]//span[@class="_1wjpf"]')
    
    for elem in caminho:
        contatos.append(elem.get_attribute("title"))
    
    return contatos
    
    
