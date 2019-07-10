import os
from peewee import *

banco = 'anim.db'
db = SqliteDatabase(banco)

class BaseModel(Model):
    class Meta: 
        database = db

class Animaizinhos(BaseModel):
    nome = CharField()
    idade = IntegerField()
    nivel_fofura = IntegerField()

if os.path.exists(banco):
    os.remove(banco)

db.connect()
db.create_tables([Animaizinhos])

kaka = Animaizinhos.create(nome = "Kamila", idade = 2, nivel_fofura = 9009999999999)

a = Animaizinhos.select()
for i in a:
    print(i.nome, i.idade, i.nivel_fofura)