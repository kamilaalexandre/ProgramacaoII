from flask import Flask, render_template, request 
app = Flask(__name__, static_url_path = "/static")

lista = [("João", "rua 9","4444-0000"), 
        ("Marina", "rua 15", "3323-4546"),
        ("Bettina", "rua 6", "9990-5980")]

@app.route("/", methods= ['POST', 'GET'])
def inicio(): 
    return render_template("inicio.html", lista=lista)

@app.route("/exibir_mensagem/")
def exibir(): 
    return render_template("exibir_mensagem.html", lista = lista)

@app.route("/listar_pessoas/")
def listar():
    return render_template("listar_pessoas.html", lista = lista)

@app.route("/incluir_pessoa/")
def incluir_pessoa():   
    nome = request.args.get("nome")
    ender = request.args.get("endereco")
    tel = request.args.get("telefone")
    nova = (nome, ender, tel)
    lista.append(nova)
    return render_template("exibir_mensagem.html", lista = lista)

@app.route("/excluir_pessoa")
def excluir(): 
    achou = None
    nome = request.args.get("nome")
    for p in lista:
        if p[0] == nome:
            achou = p 
            break
    if achou != None:
        lista.remove(achou)
    return render_template("exibir_mensagem.html", lista = lista)

if __name__ == "__main__":
    app.run(use_reloader = True, debug = True)    