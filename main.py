from flask import render_template
from app_creator import create_app

# Cria o servidor flask
app = create_app()

# Incia o servidor se o arquivo for executado
if __name__ == "__main__":
    app.run()