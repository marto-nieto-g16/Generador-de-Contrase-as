from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters  # Letras mayúsculas y minúsculas
    if use_digits:
        characters += string.digits  # Añadir dígitos
    if use_special_chars:
        special_characters = '+*-&#!¡'  # Caracteres especiales permitidos
        characters += special_characters  # Añadir caracteres especiales personalizados

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_digits = 'digits' in request.form
        use_special_chars = 'special_chars' in request.form
        password = generate_password(length, use_digits, use_special_chars)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
