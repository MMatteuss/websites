from flask import Flask, render_template, request

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template("home.html")

# Tela de download
@app.route("/jogo/Call-of-Dulty-Black-Ops")
def jogoCallOfDulty():
    call_of_dulty = str("Call of Dulty")
    return render_template("jogo.html", call_of_dulty=call_of_dulty)

# Sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# Pagina não encontrada (Erro 404)
@app.route("/<pesquisaNaoExiste>")
def pesquisaNaoExiste(pesquisaNaoExiste):
    return render_template("paginaNaoencontrada.html")











# Teste de erros
@app.route("/erros")
def erros():
    return render_template("erros.html")


# def ondeEuTo():
#     estouAqui = str
#     if erros == True:
#         estouAqui = erros
#     if sobre == True:
#         estouAqui = sobre
#     if jogoCallOfDulty == True:
#         estouAqui = jogoCallOfDulty
#     if home == True:
#         estouAqui = home





# run site
app.run(debug=True)
