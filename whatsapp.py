#Send automated whatsapp messages
from selenium import webdriver
from webzap import mandar_msg


#Abre o chrome e salva a uma variavel driver
driverPath = "C:\\Users\\tamir\\Documents\\Victor\\Subfiles_for_python_stuff\\chrome_driver\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)

#Abre a pagina do whatsapp
driver.get('https://web.whatsapp.com/')

#Variaveis pré definidas
names =  ['Tarefas', 'deutsch', 'Super Teste']
msg = 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários'
decisao = ''
vezes = 1

#Espera o usuário fazer o scan do código QR no browser para executar o resto do código
input('Pressione qualquer tecla após o scan')



#Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
print('Deseja alterar os contatos? (s/n) \nContatos atualmente: {}'.format(', '.join(names)))
decisao = input().lower()

if decisao == 's':

    names = input('''Insira os nomes dos contatos EXATAMENTE como estão no seu Whatsapp \n
                separados APENAS por virgula. ex: Joao Pedro,Maria,Jose''').split(',')
    decisao = ''
elif decisao == 'n':
    decisao = ''
    

#Recebe o nome dos usuários/grupos para quem as mensagens serão mandadas assim como a mensagem a ser mandada
print('Deseja alterar a mensagem? (s/n) \nMensagem atual: {}'.format(msg))
decisao = input().lower()
    
if decisao == 's':
    msg = input('Insira a mensagem que deseja mandar para os contatos escolhidos \n')
    decisao = ''
elif decisao == 'n':
    decisao = ''
    
print('Deseja alterar o numero de vezes? (s/n) \nNúmero de vezes atual: {}'.format(vezes))
decisao = input().lower()
    
if decisao == 's':
    vezes = input('Insira o numero de vezes que deseja mandar a mensagem: \n')
    decisao = ''
elif decisao == 'n':
    decisao = ''    
    
mandar_msg(driver, names, msg, vezes=vezes)


    
