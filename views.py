from urllib.parse import unquote_plus
from utils import load_data, load_template,save_data,build_response

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        tit = False
        for chave_valor in corpo.split('&'):
                titulo=unquote_plus(chave_valor.split('=')[0])
                descricao=unquote_plus(chave_valor.split('=')[1])
                params[titulo] = descricao
        # Carregue os dados do arquivo JSON
        save_data(params, 'notes.json')

    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return  build_response()+ load_template('index.html').format(notes=notes).encode()