import peewee, os

db = peewee.SqliteDatabase("animais.db")

class Animal(peewee.Model):
    nome_dono = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()

class Meta:
    databse = db

def __str__ (self):
    return self.tipo_animal +",", self.raca ,"de" , self.nome_dono

class Consulta(peewee.Model):
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    myID = peewee.CharField()

class Meta:
    database = db
def __str__ (self):
    return self.servico, "em" , self.data + ":" + self.horario , ",confirmado: " , \
    self.confirma , "ID da consulta: " , self.myID , "|animal: " , self.animal

if __name__ == "__main__":
    arq = ("animais.db")
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Animal, Consulta])

    except peewee.OperationalError as e:
        print("erro ao criar tabela" +str(e))

    print ("Teste do Animal")

    a1 = Animal(nomedono= "José", tipo_animal = "C", raca = "Chiuaua")
    print(a1)
    
    c1 = Consulta(data = "12/06/2019", serviço = "Aplicação de Vacina", horario = "12:00", animal = a1, confirma="N", myID='123')

    print(c1)

    print ("Teste de Persistência")
    a1.save()
    c1.save()
    c2 = Consulta(data = "21/02/2015", serviço = "Consulta de Rotina", horario = "15:00", animal = a1, confirma="S", myID='123456')
    c2.save()
    todos = Consulta.select()

    for con in todos:
        print(con)
