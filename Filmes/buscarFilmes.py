from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para recomendações
@app.route('/recomendacao', methods=['POST'])
def recomendacao():
    genero_preferido = request.form['genero']
    filmes = buscar_filmes(genero_preferido)
    return render_template('recomendacao.html', filmes=filmes)

def buscar_filmes(genero):
    url = "https://api.themoviedb.org/3/discover/movie"
    parametros = {
        'api_key': 'fc846ecb0ff88ecbe056ad1455bf9d22',
        'language': 'pt-BR',
        'sort_by': 'popularity.desc',
        'include_adult': 'false',
        'include_video': 'false',
        'page': 1,
        'with_genres': genero
    }
    resposta = requests.get(url, params=parametros)
    dados = resposta.json()
    filmes = [filme['title'] for filme in dados['results']]
    return filmes


if __name__ == '__main__':
    app.run(debug=True)
