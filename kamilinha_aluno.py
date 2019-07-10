import os
from peewee import *

banco = 'banco.db'
db = SqliteDatabase(banco)

class BaseModel(Model):
    class Meta:
        database = db  

class Aluno(BaseModel):
    nome = CharField()
    cpf = CharField()
    idade = IntegerField()

if os. path . exists (banco) :
    os. remove(banco) 
    
db.connect()
db.create_tables([Aluno])

dudu = Aluno.create(nome="Dudu", cpf= "111.243.989-70", idade  = 3)
kaka = Aluno.create(nome="Kaka", cpf= "111.243.989-70", idade = 15)
uau = Aluno.select()    
for a in uau:
    print(a.nome, a.cpf, a.idade)