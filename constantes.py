

def constantes_init():
'''
    Devolve um dicionário contendo as configurações padrão de envio (contatos, msg, vezes) e para o controle do programa principal
    
    >>>constantes_init()
    {
        'nomes' :  ['Tarefas', 'deutsch', 'Super Teste'],
        'msg' : 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários',
        'decisao' : '',
        'vezes' : 1,
        'repetir' : True   
    }
'''
    #Constantes de configuração básica
    constantes = {
        'nomes' :  ['Tarefas', 'deutsch', 'Super Teste'],
        'msg' : 'Isso é uma tentativa de mandar 1 mensagens para multiplos grupos/usuários',
        'decisao' : '',
        'vezes' : 1,
        'repetir' : True   
    }
    #Futuramente configurações de customização
    
    
    return constantes