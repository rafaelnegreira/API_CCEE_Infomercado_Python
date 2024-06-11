import requests as req

def api_infomercado_1(dataset):
    '''
    ARGUMENTOS
    dataset(string):tipo de extração de dados podendo ser por grupo('group_list'), tag('tag_list') ou package('package_list')

    FUNÇÃO
    devolve uma lista contendo o nome de todas as planilhas do infomercado.
    '''

    url1 = 'https://dadosabertos.ccee.org.br/api/3/action/' + dataset
    r = req.get(url1)
    # Resposta do servidor. Se 200 tudo ok, se 400 problema
    print(r)
    data_filter = r.json()['result']
    j = list(data_filter)
    return j

api_infomercado_1("package_list")

def api_infomercado_2(item_infomercado):
    '''
    ARGUMENTOS
    item_infomercado(string): Nome da planilha que será buscada no infomercado.

    DICAS
    (api_infomercado_1 devolve uma lista com os todos os nomes das planilhas, a intenção é adquirir o conteúdo das planilhas a partir da api_infomercado_1)
    '''
        
    url1 = 'https://dadosabertos.ccee.org.br/api/3/action/package_show?id=' + item_infomercado
    r = req.get(url1)
    print(r)
    data_filter = r.json()['result']['resources'][0]['id']
    return str(data_filter)

api_infomercado_2("acl_eol")