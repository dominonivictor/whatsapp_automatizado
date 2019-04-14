#Organizando o código
from selenium import webdriver
from time import sleep

#função para mandar 1 mensagem para diversos usuários 1 vez, com opção de aumentar o numero de mensagens
def mandar_msg(driver, names, msg, vezes=1):
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
            
        #Espera 0.5 segundos antes de passar para a próxima etapa, pois ocorreu um bug ao tentar clicar em uma mensagem
        #para outros usuarios quase ao mesmo tempo que estavam digitando e enviando a mensagem
        sleep(0.5)
