from flask import Flask, render_template, request
import openai, os, openpyxl

app = Flask(__name__)

arq = "senha.txt"
org = "org.txt"

app.config['TEMPLATES_AUTO_RELOAD'] = True

with open(arq, 'r') as arq:
    senha = arq.read()

with open(org,'r') as org:
    org = org.read()

openai.organization = os.getenv('OPENAI_ORG', org)
openai.api_key = os.getenv('OPENAI_API_KEY', senha)


@app.route('/')
def home():
    return render_template("inicio.html")



@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    data = []
    if request.method == 'POST':
        user_input = request.form.get('P1')

        if user_input:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você está falando com um chatbot do Hospital Napoleão Laureano."},
                    {"role": "user", "content": user_input},
                ]
            )
            data = response['choices'][0]['message']['content']

    return render_template("chatbot.html", data=data)


@app.route('/consultar.ramal', methods=['GET', 'POST'])
def consultar_setor():
    resposta = None
    ramal = None
    if request.method == 'POST':
        try:
            arquivo = openpyxl.load_workbook('ramais.xlsx')
            sheet = arquivo.active
            Pergunta = request.form['PR1'].upper()

            if Pergunta != "PARE":
                for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=3):
                    if Pergunta in str(row[0].value):
                        ramal = str(row[0].value)
                        resposta = str(f"O número do ramal é: {row[1].value} e fica no setor {row[2].value}")
        except KeyError:
            
            print("KeyError: 'PR1' not found in request.form")
    return render_template("chatramal.html", resposta=resposta, ramal=ramal)



if __name__ == '__main__':
    app.run(debug=True)
