#Send automated whatsapp messages
from selenium import webdriver
from webzap import mandar_msg, abre_driver

#abre uma nova janela no site do Web WhatsApp
driver = abre_driver()

#Variaveis pré definidas
names =  ['Tarefas', 'deutsch', 'Super Teste']
msg = 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários'
decisao = ''
vezes=1
repetir = True

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')


while repetir == True:
    
    names, msg, vezes = mandar_msg(driver, names, msg, vezes=vezes)
    
    print('Deseja repetir toda a operação?(s/n)') 
    
    if input().lower() == 'n': repetir = False
    


    
