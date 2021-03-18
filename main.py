from flask import render_template
from app_creator import create_app

# Cria o servidor flask
app = create_app()

titulo = "Gerenciador de Equipamento e Manutenções"

"""
    Pagina inicial
"""
@app.route('/')
def index():
    return render_template('index.html', titulo=titulo)

# Incia o servidor se o arquivo for executado
if __name__ == "__main__":
    app.run(host='0.0.0.0')