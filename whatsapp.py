#Send automated whatsapp messages
from selenium import webdriver
from webzap import mandar_msg, abre_driver, contatos_grupo
from constantes import constantes_init

#abre uma nova janela no site do Web WhatsApp
driver = abre_driver()


#Variaveis pré definidas
const = constantes_init()
nomes = const.get('nomes')
msg = const.get('msg')
vezes = const.get('vezes')
repetir = const.get('repetir')

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')


while repetir == True:   
    contatos = contatos_grupo(driver)
    if contatos: print(contatos) 

    nomes, msg, vezes = mandar_msg(driver, nomes, msg, vezes=vezes)
    
    print('Deseja repetir toda a operação?(s/n)') 
    
    if input().lower() == 'n': repetir = False
    


    
