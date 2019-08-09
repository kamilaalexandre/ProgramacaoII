"""Requisições de exame de sangue podem conter as seguintes informações:
•
a data na qual foi feita a requisição;
•
o nome do paciente;
•
o nome do médico;
•
os exames específicos solicitados (por exemplo: triglicerídeos, colesterol, etc).
Cada !!!!exame possui um nome, um preço e um prazo (em dias)!!!! para ter o resultado liberado.
Um laboratório de análises clínicas deseja controlar as requisições que recebe para realizar.
Faça as seguintes tarefas:
a)
Elabore um registro (anotações, tabelas, diagramas, etc) que permita controlar as
requisições do laboratório.
(b)
Crie classes (com uso do peewee) que permitam armazenar as informações das requisi-
ções.
(c)
Faça o teste das classes
"""
from peewee import *

db = SqliteDatabase('meubd.db')

class BaseModel(Model):
	class Meta:
		database = db

class Exame(BaseModel):
    nome = CharField()
    preco = IntegerField()
    prazo = CharField()
    
class Requisicao(BaseModel):
    data = CharField()
    nome_paciente = CharField()
    medico = CharField()
    exames = ManyToManyField(Exame)

db.connect()
db.create_tables([Exame , Requisicao, Requisicao.exames.get_through_model()])    
exame_de_sangue = Exame.create(nome = "Exame de Sangue", preco = 94, prazo = "24/04/2019")
requisicao_1 = Requisicao.create(data = "22/06/2020", nome_paciente = "Mauricio", medico = "Dr. Ricardo")
requisicao_1.exames.add(exame_de_sangue)
print(requisicao_1.nome_paciente, requisicao_1.data, requisicao.exames)