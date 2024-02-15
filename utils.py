import json
import os
def extract_route(requisicao):
    lista = requisicao.split()
    for palavra in lista:
        if palavra[0] == '/':
            retorno = palavra[1:]
            return retorno
  

def read_file(filepath):
    f= open(filepath, 'rb').read()
    return f
def load_data(filename):
    filepath = "data/"+filename
    # Abre o arquivo com o caminho correto
    with open(filepath, 'r') as arquivo_json:
        conteudo = arquivo_json.read()
        return json.loads(conteudo)
def load_template(filename):
    filepath = "templates/"+filename
    with open(filepath, 'r') as arquivo_html:
        return arquivo_html.read()
def save_data(parametros, filename):
    with open(f'data/{filename}', 'r') as arquivo:
        notas = json.load(arquivo)
    notas.append(parametros)
    with open(f'data/{filename}', 'w') as arquivo:
        json.dump(notas, arquivo, indent=2)
def build_response(body='', code=200, reason='OK', headers=''):
    if code == 302:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}\n{headers}\n{body}'.encode()