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
