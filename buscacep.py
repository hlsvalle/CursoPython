import requests

def buscar_endereco(cep):
    requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados = requisicao.json()
    return dados['logradouro'] + ', ' + dados['bairro']
    #print(dados)

if __name__ == '__main__':
    endereco = buscar_endereco('79080375')
    print(endereco)