from flask import Flask, render_template, url_for, session, request, redirect
import requests
import json

app = Flask(__name__)

# Chave secreta para o Flask trabalhar com sessões
key = 'c12390udsanc]~,kj.ç~/p;09~[65+6821323,dsdje]d~[""210o3i"ds/*-]/;.,~[==-009()((&%T¨¨$&*!@$¨#*&))]'

# Configurações de sessão
app.config['SECRET_KEY'] = key

# Global variable to store the result of the request
result = ''

# Rotas
@app.route('/')
def sobre():
    return render_template('sobre.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/central')
def central():
    global result
    
    for sport in result:
        sport["gif_path"] = f"FrontEnd/migs/{sport['name']}.gif"

    print(result)

    return render_template('central.html', resultado=result)

@app.route('/verificar', methods=['POST'])
def verificar():
    deficiency = request.form.getlist('deficiency')
    print(deficiency)
    try:
        req = requests.get('http://localhost:3000/getResult/' + '/'.join(map(str, deficiency)))
        req.raise_for_status()  # Raises an exception for 4xx and 5xx status codes

        global result
        # Convert the response text to a list of dictionaries
        result = json.loads(req.text)

        return redirect(url_for('central'))
    
    except requests.exceptions.RequestException as e:
        return "Error: Unable to fetch data from the server. Details: " + str(e)


# Botão iniciar do sobre 
@app.route('/iniciar', methods=['GET'])
def iniciar():
    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)
