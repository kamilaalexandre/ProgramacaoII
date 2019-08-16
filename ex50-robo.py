from peewee import *

db = SqliteDatabase('meubd.db')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Peca(BaseModel):
    nome = CharField()
    funcionalidade = CharField()

class Vendedor(BaseModel):
    nome = CharField()
    endereco = CharField()

class Orcamento(BaseModel):
    peca = ForeignKeyField(Peca)
    vendedor = ForeignKeyField(Vendedor)
    tempo = CharField()
    preco = IntegerField()

motor = Peca(nome = "motor de compasso", funcionalidade = "movimeta o robô")
vend1 = Vendedor(nome= "AliExpress", endereco = "aliexpress.com")
orcam1= Orcamento(peca = motor, vendedor = vend1, tempo = "7 dias", preco = 120)
print(orcam1.peca.nome,"|", orcam1.peca.funcionalidade,"|", orcam1.vendedor.nome,"|", orcam1.vendedor.endereco, "|", orcam1.tempo, "|", orcam1.preco)
vend2 = Vendedor(nome = "Presi", endereco = "Blumenau")
orcam2 = Orcamento(peca = motor, vendedor = vend2, tempo = "imediato", preco = 160)
print(orcam2.peca.nome,"|", orcam2.peca.funcionalidade,"|", orcam2.vendedor.nome,"|", orcam2.vendedor.endereco, "|", orcam2.tempo, "|", orcam2.preco)
cabo = Peca(nome= "Cabo de Aço", funcionalidade = "conectar os braços do robô com o motor")
